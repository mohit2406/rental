import pytest
import pandas as pd

@pytest.fixture(scope="session")
def load_data():
    data = pd.read_csv("../data/cleaned_data/clean_data.csv")
    return data

def test_preprocess_data():
    data = load_data()
    # data = pd.read_csv('../data/cleaned_data/clean_data.csv')
    assert len(data) > 0