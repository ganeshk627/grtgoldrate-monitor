import os
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
import email_config as ec

def send_mail(file_path=None, body=ec.body, subject=ec.subject, screenshots=None):
    msg = MIMEMultipart()
    msg['From'] = ec.send_from
    msg['To'] = ",".join(ec.send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    # msg.attach(part)

    #attaching screenshots
    if screenshots is not None:
        for f in screenshots:  # add files to the message
            file_path = os.path.join("./reports/screenshots", f)
            attachment = MIMEApplication(open(file_path, "rb").read(), _subtype="txt")
            attachment.add_header('Content-Disposition', 'attachment', filename=f)
            msg.attach(attachment)

    smtp = smtplib.SMTP_SSL(ec.smtp_server, ec.smtp_port)
    smtp.login(ec.send_from, ec.app_password)
    smtp.sendmail(ec.send_from, ec.send_to, msg.as_string())
    smtp.close()
