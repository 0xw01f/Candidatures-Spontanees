# pdf_utils.py
import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color
from io import BytesIO
from textwrap import wrap

def register_fonts(fonts):
    registered_fonts = set()
    for font in set(fonts):
        try:
            pdfmetrics.registerFont(TTFont(font, f'fonts/{font}.ttf'))
            registered_fonts.add(font)
        except:
            print(f"Unable to load font {font}. Using default font.")
    return registered_fonts

def add_text_to_pdf(input_pdf, output_pdf, texts, positions, font_sizes, colors, fonts, line_spacings, bold_texts=None):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    page = reader.pages[0]
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)

    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(width, height))
    
    registered_fonts = register_fonts(fonts + ['Poppins-Bold'])
    
    for i, (text, (x, y), font_size, color, font, line_spacing) in enumerate(zip(texts, positions, font_sizes, colors, fonts, line_spacings)):
        if font in registered_fonts:
            can.setFont(font, font_size)
        else:
            can.setFont('Helvetica', font_size)  
        can.setFillColor(Color(color[0]/255, color[1]/255, color[2]/255))
        
        if isinstance(text, list): 
            lines = text[0].split('\n')
            current_y = y
            for line in lines:
                wrapped_text = wrap(line, width=text[1])
                for wrapped_line in wrapped_text:
                    can.drawString(x, current_y, wrapped_line)
                    current_y -= font_size * line_spacing
                if not wrapped_text: 
                    current_y -= font_size * line_spacing
        else:
            if bold_texts and i in bold_texts:
                parts = text.split('**')
                current_x = x
                for k, part in enumerate(parts):
                    if k % 2 == 0: 
                        can.setFont(font if font in registered_fonts else 'Helvetica', font_size)
                    else:  
                        can.setFont('Poppins-Bold' if 'Poppins-Bold' in registered_fonts else 'Helvetica-Bold', font_size)
                    can.drawString(current_x, y, part)
                    current_x += can.stringWidth(part, can._fontname, can._fontsize)
            else:
                can.drawString(x, y, text)
    
    can.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)
    page.merge_page(new_pdf.pages[0])

    for i in range(len(reader.pages)):
        writer.add_page(reader.pages[i])

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)