
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

# Read dataset
df = pd.read_csv("students.csv")

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Separate input features
X = df[["Age", "Gender", "StudyHours"]]

# Separate target
y = df["Marks"]

# Numeric and categorical columns
numeric_features = ["Age", "StudyHours"]
categorical_features = ["Gender"]

# Preprocessing for numeric data
numeric_transformer = SimpleImputer(strategy="mean")

# Preprocessing for categorical data
categorical_transformer = OneHotEncoder(handle_unknown="ignore")

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# Apply preprocessing
X_processed = preprocessor.fit_transform(X)

print("\nProcessed Data:")
print(X_processed)

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_processed)

print("\nScaled Data:")
print(X_scaled)

# Label Encoding example
encoder = LabelEncoder()
gender_encoded = encoder.fit_transform(df["Gender"])

print("\nLabel Encoded Gender:")
print(gender_encoded)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.25, random_state=42
)

print("\nTraining Data Shape:", X_train.shape)
print("Testing Data Shape:", X_test.shape)

print("\nDay 29 Completed!")
