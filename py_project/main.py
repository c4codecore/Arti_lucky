
from send_email import send_email

email_list = [
    # ("Lucky", "coolluckyboy30@gmail.com"),
    # ("Neeraj Sharma", "nrjsrm07@gmail.com"),
    ("Arti", "artigulia1123@gmail.com")
]

formatted_email_list = []

for name, email in email_list:
    new_name = name.title()
    new_email = email.lower()
    new_tuple = (new_name, new_email)
    formatted_email_list.append(new_tuple)


with open('index.html', 'r') as file:
    html_body = file.read()

print(f"Sending email to {len(formatted_email_list)} recipients...")
send_email(html_body, formatted_email_list)
