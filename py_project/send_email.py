import smtplib                           # Built-n Python library for sending emails using SMTP protocol
from email.mime.multipart import MIMEMultipart   # Class to create a multipart email (supports both plain text and HTML)
from email.mime.text import MIMEText             # Class to create plain text or HTML text parts of an email
import logging                           # Built-in library for logging info, warnings, and errors
from config import EMAIL_USER, EMAIL_PASS    # Import email credentials from config file
from constant import SUBJECT, MESSAGE        # Import subject and message constants


def send_email(html_body, email_list):
    """
    Send personalized HTML emails to a list of recipients.
    :param html_body: The HTML email template as a string
    :param email_list: List of tuples (Name, Email) of recipients
    """

    print(f"Sending email to {len(email_list)} recipients...")

    # Check if email credentials are available
    if not EMAIL_USER or not EMAIL_PASS:
        logging.error("Email credentials are not set in environment variables.")
        return

    # Loop through each recipient in the list
    for name, to_email in email_list:
        try:
            # ---------- Create the email ----------
            msg = MIMEMultipart('alternative')   # Create a MIME email object
            msg['From'] = EMAIL_USER             # Sender email address
            msg['To'] = to_email                 # Recipient email address
            msg['Subject'] = SUBJECT             # Email subject

            # ---------- Personalize the email body ----------
            personalized_body = html_body.replace("[recipient_name]", name)  # Replace name placeholder
            personalized_body = personalized_body.replace("[message]", MESSAGE)  # Replace message placeholder
            msg.attach(MIMEText(personalized_body, 'html'))  # Attach the HTML body

            # ---------- Connect to Gmail SMTP server ----------
            server = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail SMTP server with port 587
            server.starttls()                             # Start TLS encryption
            server.login(EMAIL_USER, EMAIL_PASS)          # Login using credentials

            # ---------- Send the email ----------
            server.sendmail(EMAIL_USER, to_email, msg.as_string())
            logging.info(f"Email sent successfully from {EMAIL_USER} to {to_email}")
            print(f"Email sent successfully to {to_email}")

            # Close the SMTP server connection
            server.quit()

        except Exception as e:
            # Log error if sending email fails
            logging.error(f"Failed to send email to {to_email}: {e}")
