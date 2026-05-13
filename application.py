import streamlit as st
from fpdf import FPDF
import tempfile

st.set_page_config(page_title="AI Resume Builder", layout="centered")

st.title("🧠 AI Resume Builder")

st.write("Fill in your details and download your resume as a PDF.")

# User Inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn Profile")

summary = st.text_area("Professional Summary")

skills = st.text_area("Skills (comma separated)")

education = st.text_area("Education")

experience = st.text_area("Work Experience")

projects = st.text_area("Projects")

# Generate Resume
if st.button("Generate Resume PDF"):

    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 22)
    pdf.cell(200, 10, name, ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"{email} | {phone}", ln=True, align="C")
    pdf.cell(200, 10, linkedin, ln=True, align="C")

    pdf.ln(10)

    # Section Helper
    def section(title, content):
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, title, ln=True)

        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 8, content)

        pdf.ln(5)

    # Sections
    section("Professional Summary", summary)
    section("Skills", skills)
    section("Education", education)
    section("Work Experience", experience)
    section("Projects", projects)

    # Save PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        pdf_path = tmp_file.name

    # Download Button
    with open(pdf_path, "rb") as file:
        st.download_button(
            label="⬇ Download Resume",
            data=file,
            file_name="resume.pdf",
            mime="application/pdf"
        )

    st.success("Resume Generated Successfully!")
