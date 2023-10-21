import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587
SMTP_USERNAME = 'eleesaofficialknust@gmail.com' 
SMTP_PASSWORD = 'nuthkqhfgxuhzmmb' 
FROM_EMAIL = 'eleesaofficialknust@gmail.com'

# List of recipient email addresses
TO_EMAILS = ['keklemyevu@gmail.com', 'keklemyevu01@gmail.com']

# Create a MIMEText message (plain text)
message = MIMEMultipart()
message['From'] = FROM_EMAIL
message['To'] = ', '.join(TO_EMAILS)
message['Subject'] = 'Test Email'

# Email bodyeleesaofficialknust@gmail.com
body = 'Hello, this is a test email sent from Python.'
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Use TLS encryption
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(FROM_EMAIL, TO_EMAILS, message.as_string())
    server.quit()
    print('Email sent successfully.')
except Exception as e:
    print('Error sending email:', str(e))
