import pytest
import pandas as pd

def test_preprocess_data():
    data = pd.read_csv('../data/cleaned_data/clean_data.csv')
    assert len(data) > 0