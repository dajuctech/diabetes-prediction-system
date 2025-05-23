import pytest
from src.data.load_data import load_data
from src.data.preprocess import preprocess_data

def test_load_data():
    train_df, test_df = load_data()
    assert not train_df.empty, "Train dataset should not be empty"
    assert not test_df.empty, "Test dataset should not be empty"

def test_preprocess_data():
    train_df, _ = load_data()
    X, y = preprocess_data(train_df, target_column="Outcome")
    assert X.shape[0] == y.shape[0], "Features and labels must have matching samples"
    assert X.shape[1] > 0, "Preprocessed data should have features"
