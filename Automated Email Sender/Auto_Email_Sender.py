import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime as dt
import random
import os

# Load customer data
customers = pd.read_csv("customers.csv")

# Set up email credentials
my_email = Your Email
password =  Your Password

# Function to send email
def send_email(receiver_email, name, years, template_file):
    with open(template_file, encoding='utf-8') as letter_file:
        letter = letter_file.read()
        anniversary_letter = letter.replace("[NAME]", name).replace("[X years]", str(years))

    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = receiver_email
    msg['Subject'] = "Cheers to Another Year!"
    msg.attach(MIMEText(anniversary_letter, 'plain', 'utf-8'))  # Use UTF-8 encoding

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=receiver_email, msg=msg.as_string())

# Check for anniversaries
today = dt.datetime.now().date()
for index, customer in customers.iterrows():
    signup_date = pd.to_datetime(customer['signup_date']).date()

    # Calculate the number of years since signup
    years_since_signup = today.year - signup_date.year

    # Check if today is the anniversary of their signup
    if today.month == signup_date.month and today.day == signup_date.day and years_since_signup > 0:
        # Select a random template from the "templates" folder
        template_file = os.path.join("templates", f"email_template_{random.randint(1, 10)}.txt")
        send_email(customer['email'], customer['name'], years_since_signup, template_file)

print("Emails sent successfully!")
