import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from config import SMTP_SERVER, PORT, SENDER_EMAIL, PASSWORD, ADDITIONAL_FILES

def send_email_with_attachments(recipient_email, subject, body, attachments):
    if not all([SENDER_EMAIL, recipient_email, subject, body, attachments]):
        print(f"Incomplete email data detected for {subject}")
        return

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    for attachment in attachments:
        with open(attachment, 'rb') as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(attachment))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
        msg.attach(part)

    for file in ADDITIONAL_FILES:
        if os.path.exists(file):
            with open(file, 'rb') as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(file))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file)}"'
            msg.attach(part)
        else:
            print(f"File {file} does not exist and will not be attached.")

    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, PASSWORD)
        server.send_message(msg)

    print(f"Email sent successfully to {recipient_email}.")

# main.py
import os
import csv
from datetime import datetime
from config import CSV_FILE, CV_TEMPLATE, LM_TEMPLATE
from pdf_utils import add_text_to_pdf
from email_utils import send_email_with_attachments

def format_date(date_str):
    dt = datetime.strptime(date_str, "%d/%m/%Y")
    return dt.strftime("%d %B %Y")  # This will use the locale's month names

def generate_documents(job_name, company, cover_letter_content):
    main_folder = "generated"
    os.makedirs(main_folder, exist_ok=True)

    folder_name = os.path.join(main_folder, job_name.replace(" ", "_"))
    os.makedirs(folder_name, exist_ok=True)
    