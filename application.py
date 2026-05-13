import streamlit as st
from fpdf import FPDF
import tempfile

st.set_page_config(page_title="AI Resume Builder", layout="centered")

st.title("🧠 AI Resume Builder")

st.write("Fill in your details and download your resume as a PDF.")

# -------- Helper Function --------
# Handles special characters safely
def clean_text(text):
    if text:
        return text.encode("latin-1", "replace").decode("latin-1")
    return ""

# -------- User Inputs --------
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn Profile")

summary = st.text_area("Professional Summary")

skills = st.text_area("Skills (comma separated)")

education = st.text_area("Education")

experience = st.text_area("Work Experience")

projects = st.text_area("Projects")

# -------- Generate Resume --------
if st.button("Generate Resume PDF"):

    pdf = FPDF()
    pdf.add_page()

    # Auto page break
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title
    pdf.set_font("Arial", "B", 22)
    pdf.cell(200, 10, clean_text(name), ln=True, align="C")

    pdf.set_font("Arial", "", 12)
    pdf.cell(
        200,
        10,
        clean_text(f"{email} | {phone}"),
        ln=True,
        align="C"
    )

    pdf.cell(
        200,
        10,
        clean_text(linkedin),
        ln=True,
        align="C"
    )

    pdf.ln(10)

    # -------- Section Function --------
    def section(title, content):

        if content.strip() != "":

            pdf.set_font("Arial", "B", 16)
            pdf.cell(200, 10, clean_text(title), ln=True)

            pdf.set_font("Arial", "", 12)

            pdf.multi_cell(
                0,
                8,
                clean_text(content)
            )

            pdf.ln(5)

    # -------- Resume Sections --------
    section("Professional Summary", summary)
    section("Skills", skills)
    section("Education", education)
    section("Work Experience", experience)
    section("Projects", projects)

    # -------- Save PDF --------
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        pdf.output(tmp_file.name)
        pdf_path = tmp_file.name

    # -------- Download Button --------
    with open(pdf_path, "rb") as file:

        st.download_button(
            label="⬇ Download Resume",
            data=file,
            file_name="resume.pdf",
            mime="application/pdf"
        )

    st.success("✅ Resume Generated Successfully!")
