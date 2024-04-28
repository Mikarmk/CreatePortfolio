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
    st.header("Your Resume")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Phone: {phone}")
    st.write("**Work Experience:**")
    st.write(f"- {job_title} at {company} ({start_date.strftime('%b %Y')} - {end_date.strftime('%b %Y')})")
    st.write(job_description)
    st.write("**Education:**")
    st.write(f"- {degree} in {field_of_study} from {school} ({graduation_date.strftime('%b %Y')})")
    st.write("**Skills:**")
    for skill in skills.split(","):
        st.write(f"- {skill.strip()}")
