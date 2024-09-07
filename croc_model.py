from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import joblib
import pandas as pd
# Load the aggregated data
data = pd.read_csv('datasets/aggregated_encounter_data.csv')

# Define input features: latitude, longitude, month, year
X = data[['Latitude__', 'Longitude', 'Month', 'Year']]

# Define target variables
y_encounters = data['Encounters']  # Number of encounters
y_species = data['Species']        # Species prediction
y_size = data['Size (feet)']       # Predict size

# Train-test split
X_train, X_test, y_encounters_train, y_encounters_test = train_test_split(X, y_encounters, test_size=0.3, random_state=42)
X_train, X_test, y_species_train, y_species_test = train_test_split(X, y_species, test_size=0.3, random_state=42)
X_train, X_test, y_size_train, y_size_test = train_test_split(X, y_size, test_size=0.3, random_state=42)

# Train models for encounters, species, and size
encounter_model = RandomForestRegressor(n_estimators=100, random_state=42)
species_model = RandomForestClassifier(n_estimators=100, random_state=42)
size_model = RandomForestRegressor(n_estimators=100, random_state=42)

encounter_model.fit(X_train, y_encounters_train)
species_model.fit(X_train, y_species_train)
size_model.fit(X_train, y_size_train)

# Save the models
joblib.dump(encounter_model, 'encounter_model.pkl')
joblib.dump(species_model, 'species_model.pkl')
joblib.dump(size_model, 'size_model.pkl')
