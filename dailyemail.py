import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time


# Function to send email
def send_email():
    # Email configuration
    sender_email = "denzraymond@gmail.com"
    receiver_email = "drlacuesta@outlook.com"
    password = "Smokesdown"
    subject = "Daily Report"
    body = "This is the daily report."

    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the email body
    message.attach(MIMEText(body, "THIS IS A TEST"))

    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        # Connect to the Gmail server and send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to schedule the email sending
def schedule_daily_email():
    # Schedule the send_email function to run every day at a specific time
    schedule.every().day.at("10:20").do(send_email)  # Change the time as needed

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_daily_email()