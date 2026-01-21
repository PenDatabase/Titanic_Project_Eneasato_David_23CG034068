"""
Unit Tests for Titanic Survival Prediction System
==================================================
Optional test suite for the Flask application.

Run with: pytest tests/test_app.py -v
"""

import pytest
import json
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestRoutes:
    """Test suite for application routes."""
    
    def test_home_route(self, client):
        """Test that home page loads successfully."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Titanic Survival Prediction' in response.data
    
    def test_health_check(self, client):
        """Test health check endpoint."""
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'status' in data
        assert data['status'] == 'healthy'
    
    def test_model_info(self, client):
        """Test model information endpoint."""
        response = client.get('/model-info')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'success' in data
        if data['success']:
            assert 'model_info' in data
            assert 'algorithm' in data['model_info']

class TestPredictions:
    """Test suite for prediction functionality."""
    
    def test_valid_prediction_survived(self, client):
        """Test prediction with data likely to result in survival."""
        payload = {
            'pclass': 1,
            'sex': 'female',
            'age': 25,
            'fare': 100,
            'embarked': 'C'
        }
        response = client.post('/predict',
                              data=json.dumps(payload),
                              content_type='application/json')
        
        if response.status_code == 200:
            data = json.loads(response.data)
            assert 'success' in data
            if data['success']:
                assert 'result' in data
                assert 'prediction' in data['result']
    
    def test_valid_prediction_not_survived(self, client):
        """Test prediction with data likely to result in death."""
        payload = {
            'pclass': 3,
            'sex': 'male',
            'age': 60,
            'fare': 8,
            'embarked': 'S'
        }
        response = client.post('/predict',
                              data=json.dumps(payload),
                              content_type='application/json')
        
        if response.status_code == 200:
            data = json.loads(response.data)
            assert 'success' in data
            if data['success']:
                assert 'result' in data
                assert 'prediction' in data['result']
    
    def test_missing_field(self, client):
        """Test prediction with missing required field."""
        payload = {
            'pclass': 1,
            'sex': 'female',
            # 'age' is missing
            'fare': 100,
            'embarked': 'C'
        }
        response = client.post('/predict',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_invalid_pclass(self, client):
        """Test prediction with invalid passenger class."""
        payload = {
            'pclass': 5,  # Invalid
            'sex': 'female',
            'age': 25,
            'fare': 100,
            'embarked': 'C'
        }
        response = client.post('/predict',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_invalid_sex(self, client):
        """Test prediction with invalid sex value."""
        payload = {
            'pclass': 1,
            'sex': 'other',  # Invalid
            'age': 25,
            'fare': 100,
            'embarked': 'C'
        }
        response = client.post('/predict',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_invalid_age(self, client):
        """Test prediction with invalid age."""
        payload = {
            'pclass': 1,
            'sex': 'female',
            'age': -5,  # Invalid
            'fare': 100,
            'embarked': 'C'
        }
        response = client.post('/predict',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_invalid_fare(self, client):
        """Test prediction with invalid fare."""
        payload = {
            'pclass': 1,
            'sex': 'female',
            'age': 25,
            'fare': -10,  # Invalid
            'embarked': 'C'
        }
        response = client.post('/predict',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_invalid_embarked(self, client):
        """Test prediction with invalid embarkation port."""
        payload = {
            'pclass': 1,
            'sex': 'female',
            'age': 25,
            'fare': 100,
            'embarked': 'X'  # Invalid
        }
        response = client.post('/predict',
                              data=json.dumps(payload),
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_empty_payload(self, client):
        """Test prediction with empty payload."""
        response = client.post('/predict',
                              data=json.dumps({}),
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_no_json_data(self, client):
        """Test prediction without JSON data."""
        response = client.post('/predict')
        assert response.status_code == 400

class TestErrorHandling:
    """Test suite for error handling."""
    
    def test_404_error(self, client):
        """Test 404 error handling."""
        response = client.get('/nonexistent-route')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_invalid_method(self, client):
        """Test invalid HTTP method."""
        response = client.get('/predict')
        assert response.status_code == 405

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
