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

if st.button("Generate HTML Code"):
    html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Resume</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        h1, h2 {{
            color: #333;
        }}
        .section {{
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <h1>{name}</h1>
    <p>Email: {email}</p>
    <p>Phone: {phone}</p>

    <div class="section">
        <h2>Work Experience</h2>
        {' '.join([f"""
        <div>
            <h3>{job['job_title']} at {job['company']} ({job['start_date'].strftime('%b %Y')} - {job['end_date'].strftime('%b %Y')})</h3>
            <p>{job['job_description']}</p>
        </div>
        """ for job in work_experience])}
    </div>

    <div class="section">
        <h2>Education</h2>
        {' '.join([f"""
        <div>
            <h3>{school['degree']} in {school['field_of_study']} from {school['school']} ({school['graduation_date'].strftime('%b %Y')})</h3>
        </div>
        """ for school in education])}
    </div>

    <div class="section">
        <h2>Hard Skills</h2>
        <p>{hard_skills}</p>
    </div>

    <div class="section">
        <h2>Soft Skills</h2>
        <p>{soft_skills}</p>
    </div>
</body>
</html>
    """

    st.code(html_code, language='html')
