import csv
from send_email import send_email

email_list = []
with open("emails.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["Name"].title()
        email = row["Email"].lower()
        name_email = (name, email)
        email_list.append(name_email)


with open('index.html', 'r') as file:
    html_body = file.read()

print(f"Sending email to {len(email_list)} recipients...")
send_email(html_body, email_list)
