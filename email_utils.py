import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from config import SMTP_SERVER, PORT, SENDER_EMAIL, PASSWORD, ADDITIONAL_FILES
from rich.console import Console
from smtplib import SMTPAuthenticationError, SMTPException

console = Console()

def send_email_with_attachments(recipient_email, subject, body, attachments):
    if not all([SENDER_EMAIL, recipient_email, subject, body, attachments]):
        console.print(f"[bold red]Incomplete email data detected for {subject}. Skipping...[/bold red]")
        return

    msg = create_email_message(recipient_email, subject, body, attachments)
    
    try:
        with smtplib.SMTP(SMTP_SERVER, PORT) as server:
            server.starttls()
            try:
                server.login(SENDER_EMAIL, PASSWORD)
            except SMTPAuthenticationError as auth_error:
                console.print(f"[bold red]SMTP Authentication Error: Invalid credentials for {SENDER_EMAIL}. Please check your username and password.[/bold red]")
                console.print(f"[bold yellow]Details: {auth_error}[/bold yellow]")
                return
            server.send_message(msg)
            console.print(f"[green]Email sent successfully to {recipient_email}.[/green]")
    except SMTPException as e:
        console.print(f"[bold red]Failed to send email to {recipient_email}: {str(e)}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred while sending email: {str(e)}[/bold red]")

def create_email_message(recipient_email, subject, body, attachments):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    
    attach_files_to_email(msg, attachments)
    attach_additional_files(msg)

    return msg

def attach_files_to_email(msg, files):
    for file in files:
        with open(file, 'rb') as f:
            part = MIMEApplication(f.read(), Name=os.path.basename(file))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file)}"'
        msg.attach(part)
        console.print(f"[blue]Attached {file}[/blue]")

def attach_additional_files(msg):
    for file in ADDITIONAL_FILES:
        if os.path.exists(file):
            with open(file, 'rb') as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(file))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(file)}"'
            msg.attach(part)
            console.print(f"[blue]Attached additional file: {file}[/blue]")
        else:
            console.print(f"[bold yellow]File {file} does not exist and will not be attached.[/bold yellow]")
