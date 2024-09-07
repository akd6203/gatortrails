import pandas as pd

# Load the dataset again
file_path = 'datasets/Crocodile_Survey_Data_2021_22.xlsx'
survey_data = pd.read_excel(file_path)

# Inspect the dataset columns and drop any that are not available
print(survey_data.columns)

# Add Date, Month, and Year columns from the UTC_Date
survey_data['Date'] = pd.to_datetime(survey_data['UTC_Date']).dt.date
survey_data['Month'] = pd.to_datetime(survey_data['UTC_Date']).dt.month
survey_data['Year'] = pd.to_datetime(survey_data['UTC_Date']).dt.year

# Round latitude and longitude for grouping purposes
survey_data['Latitude__'] = survey_data['Latitude__'].round(3)
survey_data['Longitude'] = survey_data['Longitude'].round(3)

# Group by Latitude, Longitude, Date, Month, and Year and count the number of encounters
# We are not using Gender, so it's removed
encounter_data = survey_data.groupby(['Latitude__', 'Longitude', 'Date', 'Month', 'Year']).agg({
    'Species': 'first',       # Get the first species for that location and time
    'Size (feet)': 'mean'     # Get the average size of crocodiles
}).reset_index()

# Create a new column to count the number of encounters (rows) in each group
encounter_data['Encounters'] = survey_data.groupby(['Latitude__', 'Longitude', 'Date', 'Month', 'Year']).size().values

# Save the preprocessed data for further analysis
encounter_data.to_csv('datasets/aggregated_encounter_data.csv', index=False)

# Display the preprocessed data to ensure it's correct
print(encounter_data.head())
