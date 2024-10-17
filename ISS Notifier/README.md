# ISS(International Space Station) Notifier

This Python script sends an email notification 5 minutes before the International Space Station (ISS) is overhead, 
**only if it's dark** at your location. The script continuously checks every minute for the ISS's position and whether it's night, sending a notification to your email when both conditions are met.

## Features
- **ISS Location Check**: Fetches the current latitude and longitude of the ISS.
- **Sunrise-Sunset Check**: Determines if it's dark based on the local sunrise and sunset times.
- **Email Notification**: Sends an email 5 minutes before the ISS is overhead, allowing you to go outside and watch it pass.

## Prerequisites

Before you run the script, make sure you have the following:

- **Python 3.x** installed on your system.
- The following Python modules:
  - `requests` (for making API calls)
  - `smtplib` (for sending emails)
  - `time` (for timing operations)
  - `datetime` (for getting the current time)
  - `haversine` (for distance calculations)
  

  You can install the required libraries using the command:
  ```bash
  pip install requests haversine
```

If you have any questions, suggestions, or feedback, feel free to reach out.

You can contact me via:

- **Email**: [raisulislam998@gmail.com](mailto:raisulislam998@gmail.com)
- **LinkedIn**: [Raisul Islam](https://www.linkedin.com/in/contact-raisul/)
- **Facebook**: [Raisul Islam Asad](https://www.facebook.com/Raisul.Anonymous)

I'm always open to discussions and collaborations.