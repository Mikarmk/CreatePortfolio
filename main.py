import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Resume Builder", layout="wide")
st.title("Resume Builder")

# Personal Information
with st.expander("Personal Information"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

# Work Experience
with st.expander("Work Experience"):
    work_experience = []
    num_jobs = st.number_input("Number of Jobs", min_value=1, step=1, value=1)
    for i in range(int(num_jobs)):
        with st.beta_container():
            job_title = st.text_input(f"Job Title {i+1}")
            company = st.text_input(f"Company {i+1}")
            start_date = st.date_input(f"Start Date {i+1}")
            end_date = st.date_input(f"End Date {i+1}")
            job_description = st.text_area(f"Job Description {i+1}")
            work_experience.append({
                "job_title": job_title,
                "company": company,
                "start_date": start_date,
                "end_date": end_date,
                "job_description": job_description
            })

# Education
with st.expander("Education"):
    education = []
    num_schools = st.number_input("Number of Schools", min_value=1, step=1, value=1)
    for i in range(int(num_schools)):
        with st.beta_container():
            degree = st.text_input(f"Degree {i+1}")
            field_of_study = st.text_input(f"Field of Study {i+1}")
            school = st.text_input(f"School {i+1}")
            graduation_date = st.date_input(f"Graduation Date {i+1}")
            education.append({
                "degree": degree,
                "field_of_study": field_of_study,
                "school": school,
                "graduation_date": graduation_date
            })

# Skills
with st.expander("Skills"):
    hard_skills = st.text_area("Hard Skills")
    soft_skills = st.text_area("Soft Skills")

if st.button("Generate LaTeX Code"):
    latex_code = f"""
\\documentclass{{article}}
\\usepackage{{geometry}}
\\usepackage{{lipsum}}

\\title{{Resume}}
\\author{{{name}}}
\\date{{}}

\\begin{{document}}

\\maketitle

\\section{{Personal Information}}
Name: {name} \\
Email: {email} \\
Phone: {phone}

\\section{{Work Experience}}
"""

    for job in work_experience:
        latex_code += f"""
\\textbf{{{job['job_title']}}} at {job['company']} ({job['start_date'].strftime('%b %Y')} - {job['end_date'].strftime('%b %Y')}) \\
{job['job_description']}

"""

    latex_code += """\\section{{Education}}"""

    for school in education:
        latex_code += f"""
{school['degree']} in {school['field_of_study']} from {school['school']} ({school['graduation_date'].strftime('%b %Y')})

"""

    latex_code += f"""
\\section{{Hard Skills}}
{hard_skills}

\\section{{Soft Skills}}
{soft_skills}

\\end{{document}}
    """

    st.code(latex_code, language='latex')
