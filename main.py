# Workout Tracker using Google Sheets
import requests
from datetime import datetime

# INFO FOR NUTRITIONIX API

APP_ID = 'APP ID'
API_KEY = 'API KEY'
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
today = datetime.today().date()
time = datetime.now().time()

# INFO FOR SHEETY API

sheety_endpoint = 'SHEETY ENDPOINT'

# Request for Nutritionix

nutritionix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

query = input('What exercise did you do?: ')

nutritionix_body = {
    "query": query,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

exercises_data = requests.post(url=nutritionix_endpoint, headers=nutritionix_headers, json=nutritionix_body).json()['exercises'][0]

# Request for Sheety API

sheety_body = {
    'workout': {
        'date': str(today),
        'time': str(time.hour) + ':' + str(time.minute),
        'exercise': str(exercises_data['name']).title(),
        'duration': exercises_data['duration_min'],
        'calories': exercises_data['nf_calories']
    }
}

sheety_response = requests.post(url=sheety_endpoint, json=sheety_body)
print(sheety_response.status_code)


