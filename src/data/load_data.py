import pandas as pd
import os

# Define default paths
TRAIN_PATH = os.getenv("TRAIN_CSV", "data/raw/train.csv")
TEST_PATH = os.getenv("TEST_CSV", "data/raw/test.csv")

def load_data(train_path: str = TRAIN_PATH, test_path: str = TEST_PATH):
    """
    Load train and test datasets from CSV files.

    Parameters:
        train_path (str): Path to the training data CSV file.
        test_path (str): Path to the testing data CSV file.

    Returns:
        tuple: (train_df, test_df) as pandas DataFrames
    """
    try:
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)
        print(f"✅ Loaded data successfully:\n  • Train: {train_df.shape}\n  • Test: {test_df.shape}")
        return train_df, test_df
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        raise
