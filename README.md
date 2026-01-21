# 🚢 Titanic Survival Prediction System

A comprehensive machine learning web application that predicts passenger survival on the Titanic using a Random Forest Classifier.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Deployment](#deployment)
- [API Documentation](#api-documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project is a complete end-to-end machine learning application developed as part of the COS331 - Artificial Intelligence course at Covenant University. It predicts whether a passenger would have survived the Titanic disaster based on their characteristics.

**Key Highlights:**
- ✅ Production-grade code with error handling
- ✅ Clean, modern web interface
- ✅ RESTful API endpoints
- ✅ Comprehensive model evaluation
- ✅ Easy deployment to multiple platforms
- ✅ Full documentation and testing support

---

## ✨ Features

### Model Features
- **Algorithm:** Random Forest Classifier with 200 trees
- **Features Used:** Pclass, Sex, Age, Fare, Embarked
- **Accuracy:** ~82-84% on test set
- **Model Persistence:** Joblib for efficient serialization

### Application Features
- 🖥️ **Responsive Web Interface** - Works on desktop, tablet, and mobile
- 📊 **Real-time Predictions** - Instant survival probability calculations
- 📈 **Visual Feedback** - Confidence bars and probability displays
- 🔄 **Input Validation** - Comprehensive data validation and error handling
- 📱 **Modern Design** - Beautiful gradient backgrounds with ocean animations
- 🚀 **API Endpoints** - RESTful API for integration with other services
- 📉 **Model Analytics** - Display of model performance metrics

---

## 📁 Project Structure

```
Titanic_Project_yourName_matricNo/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── Titanic_hosted_webGUI_link.txt  # Deployment information
├── README.md                       # This file
│
├── model/
│   ├── model_building.ipynb        # Model training notebook
│   └── titanic_survival_model.pkl  # Trained model (generated)
│
├── static/
│   └── style.css                   # Application styling
│
├── templates/
│   └── index.html                  # Main web interface
│
└── tests/
    └── test_app.py                 # Unit tests (optional)
```

---

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/titanic-prediction.git
cd titanic-prediction
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download Dataset

1. Visit [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)
2. Download `train.csv`
3. Place it in the project root directory

### Step 5: Train the Model

```bash
jupyter notebook
# Open model/model_building.ipynb
# Run all cells to train and save the model
```

---

## 🚀 Usage

### Running Locally

```bash
python app.py
```

The application will be available at: `http://localhost:5000`

### Using the Web Interface

1. **Open the application** in your web browser
2. **Enter passenger details:**
   - Passenger Class (1st, 2nd, or 3rd)
   - Sex (Male or Female)
   - Age (in years)
   - Fare (ticket price in £)
   - Port of Embarkation (C, Q, or S)
3. **Click "Predict Survival"**
4. **View the results** including:
   - Survival prediction
   - Confidence level
   - Survival/Death probabilities
   - Input summary

### Using the API

**Make a prediction:**

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "pclass": 1,
    "sex": "female",
    "age": 25,
    "fare": 100,
    "embarked": "C"
  }'
```

**Response:**

```json
{
  "success": true,
  "result": {
    "prediction": 1,
    "prediction_label": "Survived",
    "survival_probability": 0.92,
    "death_probability": 0.08,
    "confidence": 0.92,
    "timestamp": "2026-01-21 10:30:45"
  }
}
```

---

## 🧠 Model Details

### Features Used

| Feature | Type | Description | Values |
|---------|------|-------------|--------|
| **Pclass** | Categorical | Passenger class | 1 (Upper), 2 (Middle), 3 (Lower) |
| **Sex** | Categorical | Gender | Male, Female |
| **Age** | Numerical | Age in years | 0-120 |
| **Fare** | Numerical | Ticket price | 0+ (British Pounds) |
| **Embarked** | Categorical | Port of embarkation | C (Cherbourg), Q (Queenstown), S (Southampton) |

### Preprocessing Steps

1. **Missing Value Imputation:**
   - Age: Filled with median grouped by Pclass and Sex
   - Embarked: Filled with mode (most common port)
   - Fare: Filled with median (if any missing)

2. **Feature Encoding:**
   - Sex: Binary encoding (male=1, female=0)
   - Embarked: Label encoding (C=0, Q=1, S=2)

3. **Feature Scaling:**
   - Age and Fare: StandardScaler normalization

### Model Configuration

```python
RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    max_features='sqrt',
    random_state=42,
    class_weight='balanced'
)
```

### Performance Metrics

- **Training Accuracy:** ~84-86%
- **Testing Accuracy:** ~82-84%
- **Cross-Validation Accuracy:** ~82-84% (5-fold)
- **ROC-AUC Score:** ~0.85-0.88

### Feature Importance

Based on the Random Forest model, the typical feature importance ranking:

1. **Sex** (~40-45%) - Most significant predictor
2. **Fare** (~20-25%) - Strong indicator of survival
3. **Age** (~15-20%) - Moderate importance
4. **Pclass** (~10-15%) - Moderate importance
5. **Embarked** (~5-10%) - Least important

---

## 🌐 Deployment

### Option 1: Render.com (Recommended)

1. **Create account** at [render.com](https://render.com)
2. **Connect GitHub repository**
3. **Create new Web Service**
4. **Configure:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. **Deploy!**

### Option 2: PythonAnywhere

1. **Create account** at [pythonanywhere.com](https://www.pythonanywhere.com)
2. **Upload files** via Files tab
3. **Configure web app** in Web tab
4. **Set WSGI configuration:**
   ```python
   import sys
   path = '/home/yourusername/titanic-prediction'
   if path not in sys.path:
       sys.path.append(path)
   from app import app as application
   ```
5. **Reload web app**

### Option 3: Streamlit Cloud

If you prefer Streamlit over Flask:

1. **Convert to Streamlit** (create `streamlit_app.py`)
2. **Push to GitHub**
3. **Deploy** at [streamlit.io/cloud](https://streamlit.io/cloud)

### Option 4: Heroku

1. **Create** `Procfile`:
   ```
   web: gunicorn app:app
   ```
2. **Deploy:**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

---

## 📚 API Documentation

### Endpoints

#### `GET /`
**Description:** Render the main web interface

**Response:** HTML page

---

#### `POST /predict`
**Description:** Make a survival prediction

**Request Body:**
```json
{
  "pclass": 1,
  "sex": "female",
  "age": 25,
  "fare": 100,
  "embarked": "C"
}
```

**Response:**
```json
{
  "success": true,
  "result": {
    "prediction": 1,
    "prediction_label": "Survived",
    "survival_probability": 0.92,
    "death_probability": 0.08,
    "confidence": 0.92,
    "timestamp": "2026-01-21 10:30:45",
    "input": {
      "pclass": 1,
      "sex": "Female",
      "age": 25.0,
      "fare": 100.0,
      "embarked": "C"
    }
  }
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error message description"
}
```

---

#### `GET /model-info`
**Description:** Get information about the loaded model

**Response:**
```json
{
  "success": true,
  "model_info": {
    "algorithm": "Random Forest Classifier",
    "features": ["Pclass", "Sex", "Age", "Fare", "Embarked"],
    "num_features": 5,
    "test_accuracy": 0.8324,
    "train_accuracy": 0.8456,
    "roc_auc_score": 0.8721,
    "model_loaded": true
  }
}
```

---

#### `GET /history`
**Description:** Get recent prediction history

**Response:**
```json
{
  "success": true,
  "history": [...],
  "total_predictions": 25
}
```

---

#### `GET /health`
**Description:** Health check endpoint for monitoring

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2026-01-21T10:30:45.123456"
}
```

---

## 🧪 Testing

### Sample Test Cases

```python
# Test Case 1: Rich Young Woman (Expected: Survived)
{
    "pclass": 1,
    "sex": "female",
    "age": 25,
    "fare": 100,
    "embarked": "C"
}

# Test Case 2: Poor Old Man (Expected: Did Not Survive)
{
    "pclass": 3,
    "sex": "male",
    "age": 60,
    "fare": 8,
    "embarked": "S"
}

# Test Case 3: Middle-aged Woman (Expected: Survived)
{
    "pclass": 2,
    "sex": "female",
    "age": 35,
    "fare": 30,
    "embarked": "Q"
}
```

### Running Unit Tests (Optional)

```bash
pytest tests/test_app.py -v
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**[Your Name]**
- Matric Number: [Your Matric Number]
- Course: COS331 - Artificial Intelligence
- Institution: Covenant University
- Session: 2025/2026

---

## 🙏 Acknowledgments

- **Dataset:** [Kaggle Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)
- **Institution:** Covenant University
- **Course:** COS331 - Artificial Intelligence
- **Inspiration:** Historical Titanic disaster analysis

---

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Contact your course instructor
- Email: [your.email@example.com]

---

## 🔄 Version History

- **v1.0.0** (January 2026)
  - Initial release
  - Random Forest model implementation
  - Flask web application
  - Comprehensive documentation

---

## 📊 Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Prediction Result
![Prediction Result](screenshots/result.png)

### Model Information
![Model Info](screenshots/model-info.png)

---

**⭐ If you found this project helpful, please give it a star!**

---

*Last Updated: January 21, 2026*
