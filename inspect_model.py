import joblib

encoders = joblib.load("models/encoders.pkl")
features = joblib.load("models/feature_columns.pkl")
model = joblib.load("models/themis_model.pkl")

print("\nFEATURE COLUMNS:")
print(features)

print("\nENCODER KEYS:")
print(list(encoders.keys()))

print("\nMODEL TYPE:")
print(type(model))

print("\nNUMBER OF FEATURES:")
print(model.n_features_in_)
