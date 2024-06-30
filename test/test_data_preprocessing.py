import pytest
from src.model_training import preprocess_data

def test_preprocess_data():
    raw_data = {
        'feature1': [1, 2, None, 4],
        'feature2': ['A', 'B', 'B', None]
    }
    processed_data = preprocess_data(raw_data)
    assert processed_data['feature1'].isnull().sum() == 0
    assert processed_data['feature2'].isnull().sum() == 0