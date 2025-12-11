import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(path):
    """Load dataset from a CSV file."""
    return pd.read_csv(path)

def handle_missing_values(df):
    """Fill missing values with median or mode where appropriate."""
    for col in df.columns:
        if df[col].dtype == "object":
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)
    return df

def encode_categorical(df):
    """Encode categorical features using Label Encoding."""
    le = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = le.fit_transform(df[col])
    return df

def preprocess_data(path):
    """Complete preprocessing pipeline."""
    df = load_data(path)
    df = handle_missing_values(df)
    df = encode_categorical(df)
    return df
