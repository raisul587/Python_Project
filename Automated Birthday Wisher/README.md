# Automated Birthday Wisher

This Python script automatically sends birthday wishes via email based on a CSV file containing birthday data. It checks if today matches any birthdays and sends personalized messages using predefined letter templates.

## Table of Contents
- [Requirements](#requirements)
- [How It Works](#how-it-works)
- [How to Run](#how-to-run-in-Your-Local-Machine)
- [Example CSV File](#example-csv-format)

## Requirements
Make sure you have the following libraries installed:
- `pandas`
- `random` (part of the Python standard library)
- `smtplib` (part of the Python standard library)
- `datetime` (part of the Python standard library)

You can install `pandas` using pip:
```bash
pip install pandas
```
## How It Works
The script reads birthday data from a CSV file.
Checks if today's date matches any birthdays in the csv file.
If there are matches, it selects a random letter template, personalizes it, 
and sends it via email to the respective birthday persons.

## How to Run in Your Local Machine
- Download all the files
- Modify CSV file According to Your Data
- Modify Letter According to Your Choice(Don't modify the "[NAME]" part)

## Example CSV Format
Your `csv` file should be formatted as follows:

| Name   | Email                 | Year(not mandatory) | Month | Day |
|--------|-----------------------|------|-------|-----|
| name1 | name1@gmail.com   | 2000 | 10    | 16  |
| name2   | name2@gmail.com         | 2000 | 10    | 17  |


## See You
If you have any questions, suggestions, or feedback, feel free to reach out.

You can contact me via:

- **Email**: [raisulislam998@gmail.com](mailto:raisulislam998@gmail.com)
- **LinkedIn**: [Raisul Islam](https://www.linkedin.com/in/contact-raisul/)
- **Facebook**: [Raisul Islam Asad](https://www.facebook.com/Raisul.Anonymous)

I'm always open to discussions and collaborations