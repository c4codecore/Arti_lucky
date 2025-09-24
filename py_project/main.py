import csv
from send_email import send_email   # Import the custom email sending function

# Create an empty list to store (Name, Email) tuples
email_list = []

# ---------- Read data from CSV file ----------
# Open the CSV file in read mode
with open("emails.csv", mode="r") as file:
    reader = csv.DictReader(file)   # Each row will be read as a dictionary (keys = column headers)

    # Iterate through each row in the CSV
    for row in reader:
        # Convert the name into Title Case (e.g., "neeraj sharma" -> "Neeraj Sharma")
        name = row["Name"].title()

        # Convert the email to lowercase (for consistency)
        email = row["Email"].lower()

        # Create a tuple (Name, Email)
        name_email = (name, email)

        # Add the tuple into the list
        email_list.append(name_email)

# ---------- Read HTML email template ----------
# Open and read the content of index.html file
with open('index.html', 'r') as file:
    html_body = file.read()

# Print the number of recipients
print(f"Sending email to {len(email_list)} recipients...")

# ---------- Send emails ----------
# Call the send_email function
# NOTE: send_email requires 2 arguments (html_body, email_list)
send_email(html_body, email_list)