import streamlit as st
from PIL import Image
from datetime import datetime

st.set_page_config(page_title="Resume Builder", layout="wide")
st.title("Resume Builder")

# Personal Information
with st.expander("Personal Information"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
    with col2:
        email = st.text_input("Email")
    phone = st.text_input("Phone")
    profile_pic = st.file_uploader("Upload Profile Picture", type=["jpg", "jpeg", "png"])

# Work Experience
with st.expander("Work Experience"):
    work_experience = []
    num_jobs = st.number_input("Number of Jobs", min_value=1, step=1, value=1)
    for i in range(int(num_jobs)):
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                job_title = st.text_input(f"Job Title {i+1}")
            with col2:
                company = st.text_input(f"Company {i+1}")
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input(f"Start Date {i+1}")
            with col2:
                end_date = st.date_input(f"End Date {i+1}")
            job_description = st.text_area(f"Job Description {i+1}", height=100)
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
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                degree = st.text_input(f"Degree {i+1}")
            with col2:
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
    col1, col2 = st.columns(2)
    with col1:
        hard_skills = st.text_area("Hard Skills")
    with col2:
        soft_skills = st.text_area("Soft Skills")

# Projects
with st.expander("Projects"):
    projects = []
    num_projects = st.number_input("Number of Projects", min_value=0, step=1, value=0)
    for i in range(int(num_projects)):
        with st.container():
            project_name = st.text_input(f"Project Name {i+1}")
            project_link = st.text_input(f"Project Link {i+1}")
            projects.append({
                "name": project_name,
                "link": project_link
            })

if st.button("Generate HTML Code"):
    html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Resume</title>
    <style>
        body {{
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 40px;
        }}
        .section {{
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }}
        .section h1, .section h2 {{
            color: #333;
        }}
        .job-title, .degree, .project-name {{
            font-weight: bold;
        }}
        .job-details, .education-details, .project-link {{
            color: #666;
            margin-bottom: 10px;
        }}
        .expand-btn {{
            display: block;
            width: 100%;
            text-align: right;
            color: #666;
            cursor: pointer;
        }}
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="section">
            {'<img src="data:image/png;base64,{}" width="100" height="100" />' if profile_pic else ''}
            <h1>{name}</h1>
            <p>Email: {email}</p>
            <p>Phone: {phone}</p>
        </div>

        <div class="section">
            <h2>Work Experience</h2>
            {' '.join([f"""
            <div>
                <p class="job-title">{job['job_title']} at {job['company']}</p>
                <p class="job-details">({job['start_date'].strftime('%b %Y')} - {job['end_date'].strftime('%b %Y')})</p>
                <p>{job['job_description']}</p>
            </div>
            """ for job in work_experience])}
        </div>

        <div class="section">
            <h2>Education</h2>
            {' '.join([f"""
            <div>
                <p class="degree">{school['degree']} in {school['field_of_study']}</p>
                <p class="education-details">from {school['school']} ({school['graduation_date'].strftime('%b %Y')})</p>
            </div>
            """ for school in education])}
        </div>

        <div class="section">
            <h2>Skills</h2>
            <h3>Hard Skills</h3>
            <p>{hard_skills}</p>
            <h3>Soft Skills</h3>
            <p>{soft_skills}</p>
        </div>

        {f"""
        <div class="section">
            <h2>Projects</h2>
            {' '.join([f"""
            <div>
                <p class="project-name">{project['name']}</p>
                <p class="project-link"><a href="{project['link']}" target="_blank">{project['link']}</a></p>
            </div>
            """ for project in projects])}
        </div>
        """ if projects else ""}
    </div>
</body>
</html>
    """

    st.code(html_code, language='html')
