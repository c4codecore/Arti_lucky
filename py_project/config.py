from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    filename='email_sending.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Email Credentials
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
