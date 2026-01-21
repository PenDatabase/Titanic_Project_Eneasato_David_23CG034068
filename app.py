"""
Titanic Survival Prediction Web Application
============================================
Flask-based web application for predicting Titanic passenger survival.

Author: Eneasato David Chibueze
Matric No: 23CG034068
Algorithm: Random Forest Classifier
Model Persistence: Joblib
"""

from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'titanic-survival-prediction-2026'

# Global variables
MODEL_PATH = os.path.join('model', 'titanic_survival_model.pkl')
model_package = None
prediction_history = []

def load_model():
    """Load the trained model and preprocessing objects."""
    global model_package
    try:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
        
        model_package = joblib.load(MODEL_PATH)
        print("✓ Model loaded successfully")
        print(f"  - Features: {model_package['features']}")
        print(f"  - Test Accuracy: {model_package['test_accuracy']:.4f}")
        print(f"  - ROC-AUC Score: {model_package['roc_auc']:.4f}")
        return True
    except Exception as e:
        print(f"❌ Error loading model: {str(e)}")
        return False

def validate_input(data):
    """
    Validate user input data.
    
    Parameters:
    -----------
    data : dict
        Dictionary containing passenger information
        
    Returns:
    --------
    tuple : (bool, str)
        (is_valid, error_message)
    """
    try:
        # Check required fields
        required_fields = ['pclass', 'sex', 'age', 'fare', 'embarked']
        for field in required_fields:
            if field not in data or data[field] == '':
                return False, f"Missing required field: {field}"
        
        # Validate Pclass
        pclass = int(data['pclass'])
        if pclass not in [1, 2, 3]:
            return False, "Passenger class must be 1, 2, or 3"
        
        # Validate Sex
        sex = data['sex'].lower()
        if sex not in ['male', 'female']:
            return False, "Sex must be 'male' or 'female'"
        
        # Validate Age
        age = float(data['age'])
        if age < 0 or age > 120:
            return False, "Age must be between 0 and 120"
        
        # Validate Fare
        fare = float(data['fare'])
        if fare < 0:
            return False, "Fare must be non-negative"
        
        # Validate Embarked
        embarked = data['embarked'].upper()
        if embarked not in ['C', 'Q', 'S']:
            return False, "Embarkation port must be 'C', 'Q', or 'S'"
        
        return True, "Valid"
    
    except ValueError as e:
        return False, f"Invalid data type: {str(e)}"
    except Exception as e:
        return False, f"Validation error: {str(e)}"

def preprocess_input(data):
    """
    Preprocess user input for model prediction.
    
    Parameters:
    -----------
    data : dict
        Raw input data from user
        
    Returns:
    --------
    pandas.DataFrame
        Preprocessed features ready for prediction
    """
    try:
        # Extract and convert data
        pclass = int(data['pclass'])
        sex = data['sex'].lower()
        age = float(data['age'])
        fare = float(data['fare'])
        embarked = data['embarked'].upper()
        
        # Encode sex (male=1, female=0)
        sex_encoded = 1 if sex == 'male' else 0
        
        # Encode embarked using the loaded encoder
        embarked_encoded = model_package['embarked_encoder'].transform([embarked])[0]
        
        # Create feature array in correct order
        features = model_package['features']
        feature_values = [pclass, sex_encoded, age, fare, embarked_encoded]
        
        # Create DataFrame
        input_df = pd.DataFrame([feature_values], columns=features)
        
        # Apply scaling to numerical features
        numerical_features = model_package['numerical_features']
        input_df[numerical_features] = model_package['scaler'].transform(
            input_df[numerical_features]
        )
        
        return input_df
    
    except Exception as e:
        raise ValueError(f"Preprocessing error: {str(e)}")

def make_prediction(input_df):
    """
    Make survival prediction using the loaded model.
    
    Parameters:
    -----------
    input_df : pandas.DataFrame
        Preprocessed input features
        
    Returns:
    --------
    dict
        Prediction results including class and probabilities
    """
    try:
        model = model_package['model']
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        probabilities = model.predict_proba(input_df)[0]
        
        # Prepare result
        result = {
            'prediction': int(prediction),
            'prediction_label': 'Survived' if prediction == 1 else 'Did Not Survive',
            'survival_probability': float(probabilities[1]),
            'death_probability': float(probabilities[0]),
            'confidence': float(max(probabilities)),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return result
    
    except Exception as e:
        raise ValueError(f"Prediction error: {str(e)}")

# ============================================================================
# ROUTES
# ============================================================================

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle prediction requests.
    
    Expects JSON data with passenger information.
    Returns JSON response with prediction results.
    """
    try:
        # Check if model is loaded
        if model_package is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded. Please restart the application.'
            }), 500
        
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        # Validate input
        is_valid, error_message = validate_input(data)
        if not is_valid:
            return jsonify({
                'success': False,
                'error': error_message
            }), 400
        
        # Preprocess input
        input_df = preprocess_input(data)
        
        # Make prediction
        result = make_prediction(input_df)
        
        # Add input data to result
        result['input'] = {
            'pclass': int(data['pclass']),
            'sex': data['sex'].capitalize(),
            'age': float(data['age']),
            'fare': float(data['fare']),
            'embarked': data['embarked'].upper()
        }
        
        # Store in history
        prediction_history.append(result)
        
        # Limit history size
        if len(prediction_history) > 100:
            prediction_history.pop(0)
        
        return jsonify({
            'success': True,
            'result': result
        })
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

@app.route('/model-info', methods=['GET'])
def model_info():
    """Return information about the loaded model."""
    try:
        if model_package is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded'
            }), 500
        
        info = {
            'success': True,
            'model_info': {
                'algorithm': 'Random Forest Classifier',
                'features': model_package['features'],
                'num_features': len(model_package['features']),
                'test_accuracy': float(model_package['test_accuracy']),
                'train_accuracy': float(model_package['train_accuracy']),
                'roc_auc_score': float(model_package['roc_auc']),
                'model_loaded': True
            }
        }
        
        return jsonify(info)
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/history', methods=['GET'])
def get_history():
    """Return prediction history."""
    try:
        return jsonify({
            'success': True,
            'history': prediction_history[-10:],  # Last 10 predictions
            'total_predictions': len(prediction_history)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for deployment platforms."""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model_package is not None,
        'timestamp': datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("TITANIC SURVIVAL PREDICTION SYSTEM")
    print("=" * 70)
    print("Initializing application...")
    
    # Load model
    if load_model():
        print("\n✓ Application ready!")
        print("=" * 70)
        print("\nStarting Flask server...")
        print("Access the application at: http://127.0.0.1:5000")
        print("Press CTRL+C to quit\n")
        
        # Run Flask app
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=False  # Set to False in production
        )
    else:
        print("\n❌ Failed to load model. Please ensure:")
        print(f"   1. Model file exists at: {MODEL_PATH}")
        print("   2. Model was trained using model_building.ipynb")
        print("   3. All required dependencies are installed")
        print("\nApplication cannot start without a valid model.")
