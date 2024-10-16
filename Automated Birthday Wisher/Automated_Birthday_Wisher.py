import datetime as dt
import pandas as pd
import smtplib
import random

# Get today's date (month, day)
today = (dt.datetime.now().month, dt.datetime.now().day)

# Read the birthday data
birthday_data = pd.read_csv("birthdays.csv")

# Create a dictionary with (month, day) as keys, and a list of birthday persons as values
birthday_dict = {}
for index, row in birthday_data.iterrows():
    key = (row["month"], row["day"])
    if key not in birthday_dict:
        birthday_dict[key] = [row]
    else:
        birthday_dict[key].append(row)

# Check if today matches any birthday and send emails
if today in birthday_dict:
    birthday_people = birthday_dict[today]

    # Iterate through each person with today's birthday
    for birthday_person in birthday_people:
        # Pick a random letter template and personalize it
        file = f"letter_templates/letter_{random.randint(1, 10)}.txt"
        with open(file) as letter_file:
            letter = letter_file.read()
            birthday_letter = letter.replace("[NAME]", birthday_person["name"])

        # Set up email credentials
        sender_email = "Your Email"
        password = "Your_APP_Password"
        receiver_email = birthday_person["email"]

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(
                from_addr=sender_email,
                to_addrs=receiver_email,
                msg=f"Subject:Happy Birthday\n\n{birthday_letter}"
            )
