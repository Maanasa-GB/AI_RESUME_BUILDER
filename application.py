from fpdf import FPDF
import tempfile

pdf = FPDF()
pdf.add_page()

# Add Unicode font
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", size=12)

text = """
Maanasa G B
Python Developer
• AI Projects
• Resume Builder
"""

pdf.multi_cell(0, 10, text)

tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")

pdf.output(tmp_file.name)

print("PDF Generated Successfully")
