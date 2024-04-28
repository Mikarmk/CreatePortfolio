import streamlit as st
from fpdf import FPDF

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
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, f"Name: {name}", ln=True)
    pdf.cell(200, 10, f"Email: {email}", ln=True)
    pdf.cell(200, 10, f"Phone: {phone}", ln=True)

    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, "Work Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"- {job_title} at {company} ({start_date.strftime('%b %Y')} - {end_date.strftime('%b %Y')})", ln=True)
    pdf.multi_cell(0, 10, job_description)

    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, "Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"- {degree} in {field_of_study} from {school} ({graduation_date.strftime('%b %Y')})", ln=True)

    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, "Skills", ln=True)
    pdf.set_font("Arial", size=12)
    for skill in skills.split(","):
        pdf.cell(200, 10, f"- {skill.strip()}", ln=True)

    if photo is not None:
        pdf.image(photo, x=10, y=100, w=50)

    st.write("Your resume has been generated.")
    st.write("Download your resume:")
    st.write(pdf.output(name + "_resume.pdf", dest="S").encode("latin1"), unsafe_allow_html=True)
