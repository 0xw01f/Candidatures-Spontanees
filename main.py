import os
import csv
from datetime import datetime
from config import CSV_FILE, CV_TEMPLATE, LM_TEMPLATE, JOB_NAME
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
    
    # Generate CV
    cv_title = f"CV_{job_name}_{company}.pdf".replace(" ", "_")
    cv_output = os.path.join(folder_name, cv_title)
    
    add_text_to_pdf(
        CV_TEMPLATE,
        cv_output,
        [job_name, f""],
        [(26, 780), (192, 638)],
        [11, 9],
        [(29, 155, 209), (56, 67, 71)],
        ['Poppins-Light', 'Poppins-Light'],
        [1.2, 1.2],
        bold_texts=[1]
    )
    
    # Generate cover letter
    lm_name = f"Cover_Letter_{job_name}_{company}.pdf".replace(" ", "_")
    lm_output = os.path.join(folder_name, lm_name)
    today = datetime.today().strftime("%d/%m/%Y")
    formatted_date = format_date(today)
    today = f"Date: {formatted_date}"
    add_text_to_pdf(
        LM_TEMPLATE,
        lm_output,
        [job_name, [cover_letter_content, 100], today],
        [(35, 875), (35, 840), (300, 84)],
        [18, 10, 10],
        [(30, 144, 255), (0, 0, 0), (0, 0, 0)],
        ['Poppins-Regular', 'Poppins-Regular', 'Poppins-Regular'],
        [1.2, 1.5, 1.2] 
    )

    return (cv_output, lm_output)

def main():
    # Read CSV file and store information in a list of dictionaries
  
    recipients = []
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        #! You will need a CSV file that has at least the following rows
        for row in reader:
            recipients.append({
            "firstName": row["firstName"],
            "lastName": row["lastName"],
            "fullName": row["fullName"],
            "email": row["Email"],
            "societe": row["Société"],
            "job_title": row["title"]
            })

    for recipient in recipients:
        job_name = JOB_NAME
        company = recipient['societe']

        cover_letter_content = f"""Dear {recipient['fullName'] if recipient['fullName'] else "Hiring Manager"},

Your cover letter content goes here.
"""

        documents = generate_documents(job_name, company, cover_letter_content)
        
        body = f"""
Dear {recipient['fullName'] if recipient['fullName'] else "Hiring Manager"},

Your email body content goes here.

Best regards,
Your Name
Your Contact Information
"""
    
        send_email_with_attachments(
            recipient["email"],
            f"Application for {job_name} position at {company if company else 'your company'}",
            body,
            documents  # Attachments: CV and cover letter
        )

if __name__ == "__main__":
    main()