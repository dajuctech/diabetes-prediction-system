import pytest
from src.data.load_data import load_data
from src.data.preprocess import preprocess_data
from src.model.train import train_model

def test_model_training():
    train_df, _ = load_data()
    X, y = preprocess_data(train_df, target_column="Outcome")
    
    # Use smaller data subset for faster test
    X_small, y_small = X[:100], y[:100]
    model, history = train_model(X_small, y_small, X_small, y_small)
    
    assert model is not None, "Model should not be None"
    assert hasattr(model, 'predict'), "Model should have a predict method"
