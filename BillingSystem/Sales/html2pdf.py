import pdfkit
from django.template.loader import render_to_string
from django.conf import settings
import logging

def html_to_pdf(template_src, context_dict):
    try:
        html_string = render_to_string(template_src, context_dict)
        logging.debug(f"HTML String: {html_string}")
        pdf_file = pdfkit.from_string(html_string, False, configuration=settings.PDFKIT_CONFIG)
        return pdf_file
    except Exception as e:
        logging.error(f"Error generating PDF: {e}")
        return None