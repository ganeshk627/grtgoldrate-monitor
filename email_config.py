import os

# setup 2-step verification and get app password
send_from = os.getenv('SEND_FROM')
app_password = os.getenv('APP_PASSWORD')
smtp_server = 'smtp.gmail.com'
smtp_port = 465
send_to = [os.getenv('SEND_TO')]
subject = 'GOLD RATE TODAY'
body = 'NO BODY'