from datetime import datetime
import requests as r

# App ID and API Key from Nutritionix
APP_ID = "Your APP_ID"
API_KEY = "Yor API_KEY"

# Nutritionix API endpoint for exercise tracking
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Prompt user for input
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Parameters to send to the API, including the user query and personal details
parameters = {
    "query": exercise_text,   # The exercise description from the user input
    "gender": "Male",         # Gender of the user
    "weight_kg": 52,          # Weight in kilograms
    "height_cm": 170,         # Height in centimeters
    "age": 24                 # Age of the user
}

# Send POST request to the Nutritionix API
response = r.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# Check if the response contains exercises data
if "exercises" in result:
    # Get the current date and time for logging purposes
    today_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%I:%M %p")  # 12-hour format with AM/PM

    # Google Sheets API endpoint via Sheety
    sheet_endpoint = "https://api.sheety.co/66ceecb108ab9215272318af89f33585/myWorkouts/workouts"

    # Loop through each exercise returned by the Nutritionix API
    for exercise in result["exercises"]:
        # Log each exercise (name, duration, and calories burned) for debugging
        print(f"Exercise Found: {exercise['name']}, Duration: {exercise['duration_min']} min, Calories: {exercise['nf_calories']}")

        # Prepare the data to send to Google Sheets
        sheet_inputs = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": str(exercise["duration_min"]),
                "calories": exercise["nf_calories"]
            }
        }

        # Authentication for Sheety
        user = "Your Username"
        password = "Your Password"

        # Send POST request to Sheety to log workout data in Google Sheets
        sheet_response = r.post(sheet_endpoint, json=sheet_inputs, auth=(user, password))

        # Sheety response for each exercise logged
        print(sheet_response.text)

    print("All exercises processed.")
else:
    # Print error message if no exercises were found in the API response
    print(f"Error: {result.get('message', 'No exercises found in response')}")
