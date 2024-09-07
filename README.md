# GatorTrails - Crocodile Activity Predictor

### Overview

**GatorTrails** is a web application built using Flask that allows users to predict crocodile encounters based on location and time. The app offers a user-friendly interface where users can click on a map to select a location, specify a month and year, and then receive predictions for the likelihood of crocodile encounters, estimated size of the crocodile, and species information. Additionally, the app integrates with Wikipedia to provide further details about the predicted crocodile species.
![GatorTrails Homepage](static/snapshot.png)

### Key Features

- **Map-Based Interaction**: Users can easily select a location by clicking on a map, making the process intuitive and accessible.
- **Crocodile Predictions**: The app uses machine learning models to predict the number of crocodile encounters, the species, and the size of the crocodile.
- **Species Information**: The app fetches additional information about the predicted crocodile species from Wikipedia, giving users a comprehensive view.
- **Responsive Design**: Built using Bootstrap, the app is responsive and works across different devices.

---

## Background

The Northern Territory of Australia is known for its rich wildlife, including a significant population of saltwater crocodiles. This app aims to help residents and tourists predict potential crocodile encounters in specific areas, promoting awareness and safety. The application utilizes historical data on crocodile encounters to provide predictions based on location and time.

---

## Data Preprocessing

The raw dataset we worked with contained several records of crocodile sightings and captures across various regions. However, the data needed to be transformed and cleaned before it could be used for predictive modeling. Here's an outline of how we processed the data:

1. **Data Cleaning**: We began by removing any incomplete or duplicate records. Many rows contained missing information, especially in location fields, which were critical for the model's accuracy.
   
2. **Feature Engineering**: To prepare the data for model training, we extracted important features such as:
   - **Latitude and Longitude**: To pinpoint the specific location of encounters.
   - **Month and Year**: To track time-based trends in crocodile sightings and encounters.
   - **Species and Size**: These were used to provide richer predictions.
   
3. **Aggregation**: The raw data often contained multiple records for the same location and time period. To make the data more useful for predictions, we grouped the data by location (latitude, longitude), month, and year. We then computed summary statistics like the number of encounters and the average size of crocodiles in each area.

4. **Data Scaling**: Some of the features had different units or ranges, so we standardized the data to ensure that the machine learning models could make accurate predictions without being biased by scale.

---

## Machine Learning Models

We used three machine learning models to make predictions:
1. **Encounter Prediction Model**: This model predicts the number of crocodile encounters for a given location and time.
2. **Species Prediction Model**: This classification model predicts the species of the crocodile most likely to be encountered based on location and time.
3. **Size Prediction Model**: This model predicts the average size of the crocodile at the selected location and time.

The models were trained using the preprocessed data, and the predictions are made in real-time when the user selects a location and provides a month and year.

---

## How It Works

1. **Select a Location**: Users interact with an interactive map where they can click on a location of interest.
2. **Input Date**: Users specify the month and year for which they want predictions.
3. **View Predictions**: The app uses pre-trained machine learning models to predict the likelihood of encountering crocodiles, the species, and their size. Additional species information is fetched from Wikipedia for a richer user experience.

---

## Running the Project

### Prerequisites

To run this project locally, you need:
- **Python 3.x**
- **Flask** installed on your machine
- The necessary dependencies listed in `requirements.txt`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/akd6203/gatortrails.git
   cd gatortrails
2. Set up a virtual environment:
  python3 -m venv venv
  source venv/bin/activate    # On Windows: venv\Scripts\activate
3. Install the dependencies:
   pip install -r requirements.txt
4. Run the Flask application:
   flask run
The app will be available at http://127.0.0.1:5000/

### Contributing

Contributions are welcome! If you find any issues or have ideas for improvement, feel free to submit a pull request or open an issue. Happy Coding!!!
