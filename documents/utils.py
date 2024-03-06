from fpdf import FPDF, HTMLMixin
from html import unescape
from io import BytesIO
from .models import Document


class MyFPDF(FPDF, HTMLMixin):
    def write_html(self, text, image_map=None):
        h2p = HTML2FPDF(self, image_map)
        h2p.feed(text)

def generate_pdf(document_id):
    try:
        document = Document.objects.get(pk=document_id)  # Use pk for primary key lookup
    except Document.DoesNotExist:
        return None  # Return None on document not found (graceful error handling)

    buffer = BytesIO()
    pdf = MyFPDF()
    pdf.add_page()

    # Generate dynamic HTML content from document data
    html_content = f"""
    <h1>{document.header}</h1>
    <p>{document.body}</p>  # Add other relevant document fields
    """

    pdf.write_html(html_content)
    pdf.output(buffer, 'F')
    return buffer.getvalue()