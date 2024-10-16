from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color
from io import BytesIO
from textwrap import wrap
import os


from datetime import datetime

def format_date(date_str):
    dt = datetime.strptime(date_str, "%d/%m/%Y")
    return dt.strftime("%d %B %Y")
def generate_cv(folder_name, job_name, company):
    cv_title = f"CV_{job_name}_{company}.pdf".replace(" ", "_")
    cv_output = os.path.join(folder_name, cv_title)
    
    add_text_to_pdf(
        "cv_template.pdf",
        cv_output,
        [job_name, ""],
        [(26, 780), (192, 638)],
        [11, 9],
        [(29, 155, 209), (56, 67, 71)],
        ['Poppins-Light', 'Poppins-Light'],
        [1.2, 1.2],
        bold_texts=[1]
    )
    return cv_output

def generate_cover_letter(folder_name, job_name, company, cover_letter_content):
    lm_name = f"Cover_Letter_{job_name}_{company}.pdf".replace(" ", "_")
    lm_output = os.path.join(folder_name, lm_name)
    today = format_date(datetime.today().strftime("%d/%m/%Y"))

    add_text_to_pdf(
        "lm_template.pdf",
        lm_output,
        [job_name, [cover_letter_content, 100], f"Date: {today}"],
        [(35, 875), (35, 840), (300, 84)],
        [18, 10, 10],
        [(30, 144, 255), (0, 0, 0), (0, 0, 0)],
        ['Poppins-Regular', 'Poppins-Regular', 'Poppins-Regular'],
        [1.2, 1.5, 1.2]
    )
    return lm_output

def add_text_to_pdf(input_pdf, output_pdf, texts, positions, font_sizes, colors, fonts, line_spacings, bold_texts=None):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    page = reader.pages[0]
    width, height = float(page.mediabox.width), float(page.mediabox.height)

    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(width, height))
    
    registered_fonts = register_fonts(fonts + ['Poppins-Bold'])
    
    for i, (text, (x, y), font_size, color, font, line_spacing) in enumerate(zip(texts, positions, font_sizes, colors, fonts, line_spacings)):
        set_font_and_color(can, font, font_size, color, registered_fonts)
        draw_text(can, text, x, y, font_size, line_spacing, bold_texts, i, registered_fonts)
    
    can.save()
    packet.seek(0)

    new_pdf = PdfReader(packet)
    page.merge_page(new_pdf.pages[0])
    writer.add_page(page)

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

def set_font_and_color(can, font, font_size, color, registered_fonts):
    can.setFont(font if font in registered_fonts else 'Helvetica', font_size)
    can.setFillColor(Color(color[0]/255, color[1]/255, color[2]/255))

def draw_text(can, text, x, y, font_size, line_spacing, bold_texts, index, registered_fonts):
    if isinstance(text, list):
        wrap_text(can, text[0], text[1], x, y, font_size, line_spacing)
    else:
        if bold_texts and index in bold_texts:
            draw_bold_text(can, text, x, y, font_size, registered_fonts)
        else:
            can.drawString(x, y, text)

def wrap_text(can, text, width, x, y, font_size, line_spacing):
    lines = text.split('\n')
    current_y = y
    for line in lines:
        wrapped_text = wrap(line, width=width)
        for wrapped_line in wrapped_text:
            can.drawString(x, current_y, wrapped_line)
            current_y -= font_size * line_spacing
        if not wrapped_text:
            current_y -= font_size * line_spacing

def draw_bold_text(can, text, x, y, font_size, registered_fonts):
    parts = text.split('**')
    current_x = x
    for i, part in enumerate(parts):
        if i % 2 == 0:
            can.setFont(can._fontname, font_size)
        else:
            can.setFont('Poppins-Bold' if 'Poppins-Bold' in registered_fonts else 'Helvetica-Bold', font_size)
        can.drawString(current_x, y, part)
        current_x += can.stringWidth(part, can._fontname, can._fontsize)

def register_fonts(fonts):
    registered_fonts = set()
    for font in set(fonts):
        try:
            pdfmetrics.registerFont(TTFont(font, f'fonts/{font}.ttf'))
            registered_fonts.add(font)
        except:
            print(f"Unable to load font {font}. Using default font.")
    return registered_fonts
