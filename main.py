import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from PIL import Image
import io

st.set_page_config(page_title="Resume Builder")
st.title("Resume Builder")

# Personal Information
st.header("Personal Information")
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
photo = st.file_uploader("Upload Photo", type=["jpg", "jpeg", "png"])

# Work Experience
st.header("Work Experience")
with st.expander("Add Work Experience"):
    job_title = st.text_input("Job Title")
    company = st.text_input("Company")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    job_description = st.text_area("Job Description")

# Education
st.header("Education")
with st.expander("Add Education"):
    degree = st.text_input("Degree")
    field_of_study = st.text_input("Field of Study")
    school = st.text_input("School")
    graduation_date = st.date_input("Graduation Date")

# Skills
st.header("Skills")
with st.expander("Add Skills"):
    skills = st.text_area("Skills")

if st.button("Generate Resume"):
    # Create a BytesIO object to hold the LaTeX data
    latex_bytes = io.BytesIO()

    # Create the LaTeX document
    doc = SimpleDocTemplate(latex_bytes, pagesize=letter)
    styles = getSampleStyleSheet()

    # Add personal information
    elements = []
    elements.append(Paragraph(name, styles["Heading1"]))
    elements.append(Paragraph(email, styles["BodyText"]))
    elements.append(Paragraph(phone, styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Add work experience
    elements.append(Paragraph("Work Experience", styles["Heading2"]))
    elements.append(Paragraph(f"{job_title} at {company} ({start_date.strftime('%b %Y')} - {end_date.strftime('%b %Y')})", styles["BodyText"]))
    elements.append(Paragraph(job_description, styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Add education
    elements.append(Paragraph("Education", styles["Heading2"]))
    elements.append(Paragraph(f"{degree} in {field_of_study} from {school} ({graduation_date.strftime('%b %Y')})", styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Add skills
    elements.append(Paragraph("Skills", styles["Heading2"]))
    for skill in skills.split(","):
        elements.append(Paragraph(f"- {skill.strip()}", styles["BodyText"]))
    elements.append(Spacer(1, 12))

    # Add photo if available
    if photo is not None:
        image = Image.open(photo)
        image.thumbnail((1 * inch, 1 * inch))
        img_data = io.BytesIO()
        image.save(img_data, format='PNG')
        elements.append(Image(img_data, width=1 * inch, height=1 * inch))
        elements.append(Spacer(1, 12))

    # Build the PDF
    doc.build(elements)

    # Allow the user to download the LaTeX file
    st.download_button(
        label="Download Resume",
        data=latex_bytes.getvalue(),
        file_name=f"{name}_resume.tex",
        mime="application/x-tex",
    )
