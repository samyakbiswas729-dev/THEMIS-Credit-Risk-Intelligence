import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# =====================================

# LOAD DATASET

# =====================================

df = pd.read_csv("data/german_credit_data.csv")

print("Dataset Shape:", df.shape)

# =====================================

# FEATURE ENGINEERING

# =====================================

df["credit_per_month"] = (
df["credit_amount"] / df["month_duration"]
)

df["high_credit_flag"] = (
df["credit_amount"] > df["credit_amount"].median()
).astype(int)

# =====================================

# TARGET ENCODING

# =====================================

target_encoder = LabelEncoder()

df["target"] = target_encoder.fit_transform(
df["target"]
)

# =====================================
# CATEGORICAL ENCODING
# =====================================

encoders = {}

categorical_cols = df.select_dtypes(
    include=["object", "string"]
).columns.tolist()

print("\nCategorical Columns:")
print(categorical_cols)

for col in categorical_cols:
    encoder = LabelEncoder()

    df[col] = encoder.fit_transform(
        df[col].astype(str)
    )

    encoders[col] = encoder

# =====================================

# FEATURES & TARGET

# =====================================

X = df.drop("target", axis=1)

y = df["target"]

# Save feature order

joblib.dump(
list(X.columns),
"models/feature_columns.pkl"
)

# =====================================

# TRAIN TEST SPLIT

# =====================================

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.20,
random_state=42,
stratify=y
)

# =====================================

# MODEL TRAINING

# =====================================

model = RandomForestClassifier(
n_estimators=300,
max_depth=10,
random_state=42
)

model.fit(X_train, y_train)

# =====================================

# PREDICTIONS

# =====================================

pred = model.predict(X_test)

accuracy = accuracy_score(
y_test,
pred
)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(
classification_report(
y_test,
pred
)
)

# =====================================

# SAVE MODEL FILES

# =====================================

joblib.dump(
model,
"models/themis_model.pkl"
)

joblib.dump(
encoders,
"models/encoders.pkl"
)

joblib.dump(
target_encoder,
"models/target_encoder.pkl"
)

print("\nModel Saved Successfully")
print("Encoders Saved Successfully")
print("Target Encoder Saved Successfully")
print("Feature Columns Saved Successfully")
