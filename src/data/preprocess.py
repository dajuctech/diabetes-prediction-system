import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import SMOTE, RandomOverSampler
from sklearn.model_selection import train_test_split

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill or drop missing values."""
    # Example: fill numeric columns with median
    df.fillna(df.median(numeric_only=True), inplace=True)
    return df

def encode_categoricals(df: pd.DataFrame) -> pd.DataFrame:
    """Encode categorical features."""
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column].astype(str))
    return df

def scale_features(X: pd.DataFrame) -> pd.DataFrame:
    """Standardize numerical features."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return pd.DataFrame(X_scaled, columns=X.columns)

def apply_oversampling(X: pd.DataFrame, y: pd.Series, method="smote"):
    """Balance dataset using SMOTE or RandomOverSampler."""
    if method == "smote":
        sampler = SMOTE(random_state=42)
    elif method == "random":
        sampler = RandomOverSampler(random_state=42)
    else:
        raise ValueError("Unsupported method. Use 'smote' or 'random'.")
    X_res, y_res = sampler.fit_resample(X, y)
    return X_res, y_res

def preprocess_data(df: pd.DataFrame, target_column: str, oversample: bool = True):
    """
    Full preprocessing pipeline:
    - Handle missing values
    - Encode categoricals
    - Scale features
    - Apply SMOTE or ROS if enabled
    """
    df = handle_missing_values(df)
    df = encode_categoricals(df)

    X = df.drop(columns=[target_column])
    y = df[target_column]

    X = scale_features(X)

    if oversample:
        X, y = apply_oversampling(X, y, method="smote")

    return X, y
