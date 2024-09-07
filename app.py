from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import requests

app = Flask(__name__)

# Load the pre-trained models
encounter_model = joblib.load('encounter_model.pkl')
species_model = joblib.load('species_model.pkl')
size_model = joblib.load('size_model.pkl')

# Function to get species details from Wikipedia
def get_species_details(species_name):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{species_name.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    lat = float(request.form['latitude'])
    lon = float(request.form['longitude'])
    month = int(request.form['month'])
    year = int(request.form['year'])
    
    # Prepare input data for predictions
    input_data = pd.DataFrame([[lat, lon, month, year]], columns=['Latitude__', 'Longitude', 'Month', 'Year'])
    
    # Predict the number of encounters, species, and size
    predicted_encounters = encounter_model.predict(input_data)
    predicted_species = species_model.predict(input_data)
    predicted_size = size_model.predict(input_data)
    
    # Get species details from Wikipedia
    species_details = get_species_details(predicted_species[0])
    
    return jsonify({
        'latitude': lat,
        'longitude': lon,
        'month': month,
        'year': year,
        'predicted_encounters': int(predicted_encounters[0]),
        'predicted_species': predicted_species[0],
        'predicted_size': round(predicted_size[0], 2),
        'species_details': species_details
    })

if __name__ == '__main__':
    app.run(debug=True)
