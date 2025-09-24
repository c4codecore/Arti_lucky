import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
from config import EMAIL_USER, EMAIL_PASS
from constant import SUBJECT, MESSAGE


def send_email(html_body, email_list):
   
    print(f"Sending email to {len(email_list)} recipients...")

    if not EMAIL_USER or not EMAIL_PASS:
        logging.error("Email credentials are not set in environment variables.")
        return

    for name, to_email in email_list:
        try:
            # Create email message
            msg = MIMEMultipart('alternative')
            msg['From'] = EMAIL_USER
            msg['To'] = to_email
            msg['Subject'] = SUBJECT

            # Personalize email body
            personalized_body = html_body.replace("[recipient_name]", name)
            personalized_body = personalized_body.replace("[message]", MESSAGE)
            msg.attach(MIMEText(personalized_body, 'html'))

            # Send email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, to_email, msg.as_string())
            logging.info(f"Email sent successfully to {to_email}")
            print(f"Email sent successfully to {to_email}")
            server.quit()
        except Exception as e:
            logging.error(f"Failed to send email to {to_email}: {e}")
