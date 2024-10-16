import os
import csv
from datetime import datetime
from config import CSV_FILE, CV_TEMPLATE, LM_TEMPLATE, JOB_NAME
from pdf_utils import generate_cv, generate_cover_letter
from email_utils import send_email_with_attachments
from rich.console import Console

console = Console()

def format_date(date_str):
    dt = datetime.strptime(date_str, "%d/%m/%Y")
    return dt.strftime("%d %B %Y")

def generate_documents(job_name, company, cover_letter_content):
    folder_name = create_output_folder(job_name)
    
    console.print(f"[bold cyan]Generating documents for {company}...[/bold cyan]")
    
    cv_output = generate_cv(folder_name, job_name, company)
    lm_output = generate_cover_letter(folder_name, job_name, company, cover_letter_content)

    return cv_output, lm_output

def create_output_folder(job_name):
    main_folder = "generated"
    folder_name = os.path.join(main_folder, job_name.replace(" ", "_"))
    os.makedirs(folder_name, exist_ok=True)
    console.print(f"[green]Created folder: {folder_name}[/green]")
    return folder_name

def load_recipients(csv_file):
    console.print(f"[bold yellow]Loading recipients from {csv_file}...[/bold yellow]")
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        recipients = [
            {
                "firstName": row["firstName"],
                "lastName": row["lastName"],
                "fullName": row["fullName"] or "Hiring Manager",
                "email": row["Email"],
                "societe": row["Société"],
                "job_title": row["title"]
            }
            for row in reader
        ]
    console.print(f"[green]Loaded {len(recipients)} recipients.[/green]")
    return recipients

def main():
    from rich.console import Console

console = Console()

banner = """
   ___                _ _     _       _                             __                   _                             
  / __\__ _ _ __   __| (_) __| | __ _| |_ _   _ _ __ ___  ___      / _\_ __   ___  _ __ | |_ __ _ _ __   ___  ___  ___ 
 / /  / _` | '_ \ / _` | |/ _` |/ _` | __| | | | '__/ _ \/ __|_____\ \| '_ \ / _ \| '_ \| __/ _` | '_ \ / _ \/ _ \/ __|
/ /__| (_| | | | | (_| | | (_| | (_| | |_| |_| | | |  __/\__ \_____|\ \ |_) | (_) | | | | || (_| | | | |  __/  __/\__ \\
\____/\__,_|_| |_|\__,_|_|\__,_|\__,_|\__|\__,_|_|  \___||___/     \__/ .__/ \___/|_| |_|\__\__,_|_| |_|\___|\___||___/
                                                                      |_|                                              
"""

console.print(banner, style="cyan")
console.print("[bold magenta]Starting the application process...[/bold magenta]")
recipients = load_recipients(CSV_FILE)
for recipient in recipients:
    job_name = JOB_NAME
    company = recipient['societe']
    cover_letter_content = f"Dear {recipient['fullName']},\n\nYour cover letter content goes here."
    # Generate documents
    documents = generate_documents(job_name, company, cover_letter_content)
    
    # Prepare email body and send email
    body = f"""
    Dear {recipient['fullName']},
    Your email body content goes here.
    Best regards,
    Your Name
    Your Contact Information
    """

    console.print(f"[blue]Sending email to {recipient['email']}...[/blue]")
    send_email_with_attachments(
        recipient["email"],
        f"Application for {job_name} position at {company if company else 'your company'}",
        body,
        documents
    )
    console.print(f"[green]Email sent to {recipient['email']}.[/green]")
console.print("[bold magenta]All emails have been sent![/bold magenta]")

if __name__ == "__main__":
    main()
