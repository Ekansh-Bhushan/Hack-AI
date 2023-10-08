import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# Function to send email alerts
def send_email_alert(receiver_email, subject, message):
    # Replace with your SMTP server details
    smtp_server = input("Enter your email:")
    smtp_port = 587
    smtp_username = input("Enter your username:")
    smtp_password = input("Enter your password:")
    smtp_dob=input("Enter The dob (dd-mm-yyyy) : ")
    def is_validate_date(smtp_dob):
    fields = smtp_dob.split("-")
    contains_all_fields = len(fields) == 3
    all_fields_are_integers = all([field.isdigit() for field in fields])
    return contains_all_fields and all_fields_are_integers


def get_dob():
    while True:
        if is_validate_date(smtp_dob):
            day, month, year = [int(field) for field in date.split("-")]
            try:
                smtp_dob = datetime(year, month, day)
                if smtp_dob > datetime.today():
                    raise ValueError
                return smtp_dob
            except ValueError:
                print("The Date You Entered Doesn't Exists, Or it is grater than today. Try That Again...")
        else:
            print("Your Answer Might Not Be In The Mentioned Date Format, Try That Again...")

    
    # Create a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    
    # Create an email message
    email_message = MIMEMultipart()
    email_message['From'] = smtp_username
    email_message['To'] = receiver_email
    email_message['Subject'] = subject
    
    # Add the message body
    email_message.attach(MIMEText(message, 'plain'))
    
    # Send the email
    server.sendmail(smtp_username, receiver_email, email_message.as_string())
    
    # Close the SMTP server connection
    server.quit()

# Example usage with random input values
if __name__ == '__main__':
    # Generate a random email address for testing
    random_email = f'user{random.randint(1, 100)}@example.com'
    subject = 'Currency Exchange Rate Alert'
    message = 'The exchange rate has crossed your defined threshold.'
    
    try:
        send_email_alert(random_email, subject, message)
        print(f'Alert email sent to {random_email}')
    except Exception as e:
        print(f'Error sending email: {str(e)}')

#alternative code

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email alerts
def send_email_alert(receiver_email, subject, message):
    # Replace with your SMTP server details
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    smtp_username = 'your_username'
    smtp_password = 'your_password'
    
    # Create a connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    
    # Create an email message
    email_message = MIMEMultipart()
    email_message['From'] = smtp_username
    email_message['To'] = receiver_email
    email_message['Subject'] = subject
    
    # Add the message body
    email_message.attach(MIMEText(message, 'plain'))
    
    # Send the email
    server.sendmail(smtp_username, receiver_email, email_message.as_string())
    
    # Close the SMTP server connection
    server.quit()

# Function to check and send alerts
def check_and_send_alerts(base_currency, foreign_currency, current_rate, alert_threshold):
    if current_rate > alert_threshold:
        subject = f'Exchange Rate Alert: {base_currency} to {foreign_currency}'
        message = f'The exchange rate {base_currency} to {foreign_currency} has crossed {alert_threshold}.'
        # Replace with the user's email address
        receiver_email = 'user@example.com'
        try:
            send_email_alert(receiver_email, subject, message)
            print(f'Alert email sent to {receiver_email}')
        except Exception as e:
            print(f'Error sending email: {str(e)}')

# Example usage
if __name__ == '__main__':
    base_currency = 'USD'
    foreign_currency = 'EUR'
    current_rate = 1.19  # Replace with the actual exchange rate
    alert_threshold = 1.20  # Set the threshold for the alert
    
    check_and_send_alerts(base_currency, foreign_currency, current_rate, alert_threshold)
