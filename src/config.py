"""
App constants: paths, the random seed, and column names.
Single source of truth :)
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = PROJECT_ROOT / "data" / "diabetes_data_upload.csv"
MODEL_DIR = PROJECT_ROOT / "model"
TEST_DATA_PATH = PROJECT_ROOT / "test_data.csv"

SEED = 5598
TEST_SIZE = 0.2

TARGET = "class"
POSITIVE_LABEL = "Positive"
NEGATIVE_LABEL = "Negative"

# Column names areas in CSV header
NUMERIC_FEATURES = ["Age"]

GENDER_FEATURE = "Gender"  # Male/Female — encoded separately from the Yes/No flags

BINARY_FEATURES = [
    "Polyuria",
    "Polydipsia",
    "sudden weight loss",
    "weakness",
    "Polyphagia",
    "Genital thrush",
    "visual blurring",
    "Itching",
    "Irritability",
    "delayed healing",
    "partial paresis",
    "muscle stiffness",
    "Alopecia",
    "Obesity",
]

FEATURES = NUMERIC_FEATURES + [GENDER_FEATURE] + BINARY_FEATURES
