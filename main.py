import streamlit as st

st.set_page_config(page_title="Resume Builder")
st.title("Resume Builder")

# Personal Information
st.header("Personal Information")
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")

# Work Experience
st.header("Work Experience")
job_title = st.text_input("Job Title")
company = st.text_input("Company")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
job_description = st.text_area("Job Description")

# Education
st.header("Education")
degree = st.text_input("Degree")
field_of_study = st.text_input("Field of Study")
school = st.text_input("School")
graduation_date = st.date_input("Graduation Date")

# Skills
st.header("Skills")
skills = st.text_area("Skills")

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
\\textbf{{{job_title}}} at {company} ({start_date.strftime('%b %Y')} - {end_date.strftime('%b %Y')}) \\
{job_description}

\\section{{Education}}
{degree} in {field_of_study} from {school} ({graduation_date.strftime('%b %Y')})

\\section{{Skills}}
{skills}

\\end{{document}}
    """

    st.code(latex_code, language='latex')
