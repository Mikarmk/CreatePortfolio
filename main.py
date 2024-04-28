import streamlit as st
from PIL import Image
from datetime import datetime

st.set_page_config(page_title="Создатель Резюме", layout="wide")
st.title("Создатель Резюме")

# Личная информация
with st.expander("Личная информация"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Имя", key="name")
    with col2:
        email = st.text_input("Электронная почта", key="email")
    phone = st.text_input("Телефон", key="phone")
    profile_pic = st.file_uploader("Загрузить фото профиля", type=["jpg", "jpeg", "png"], key="profile_pic")

# Опыт работы
with st.expander("Опыт работы"):
    work_experience = []
    num_jobs = st.number_input("Количество мест работы", min_value=1, step=1, value=1, key="num_jobs")
    for i in range(int(num_jobs)):
        with st.container():
            job_title = st.text_input(f"Должность {i+1}", key=f"job_title_{i}")
            company = st.text_input(f"Компания {i+1}", key=f"company_{i}")
            start_date = st.date_input(f"Дата начала {i+1}", key=f"start_date_{i}")
            end_date = st.date_input(f"Дата окончания {i+1}", key=f"end_date_{i}")
            job_description = st.text_area(f"Описание работы {i+1}", height=100, key=f"job_description_{i}")
            work_experience.append({
                "job_title": job_title,
                "company": company,
                "start_date": start_date,
                "end_date": end_date,
                "job_description": job_description
            })

# Образование
with st.expander("Образование"):
    education = []
    num_schools = st.number_input("Количество учебных заведений", min_value=1, step=1, value=1, key="num_schools")
    for i in range(int(num_schools)):
        with st.container():
            degree = st.text_input(f"Степень {i+1}", key=f"degree_{i}")
            field_of_study = st.text_input(f"Направление {i+1}", key=f"field_of_study_{i}")
            school = st.text_input(f"Учебное заведение {i+1}", key=f"school_{i}")
            graduation_date = st.date_input(f"Дата окончания {i+1}", key=f"graduation_date_{i}")
            education.append({
                "degree": degree,
                "field_of_study": field_of_study,
                "school": school,
                "graduation_date": graduation_date
            })

# Навыки
with st.expander("Навыки"):
    col1, col2 = st.columns(2)
    with col1:
        hard_skills = st.text_area("Профессиональные навыки", key="hard_skills")
    with col2:
        soft_skills = st.text_area("Личные качества", key="soft_skills")

# Проекты
with st.expander("Проекты"):
    projects = []
    num_projects = st.number_input("Количество проектов", min_value=0, step=1, value=0, key="num_projects")
    for i in range(int(num_projects)):
        with st.container():
            project_name = st.text_input(f"Название проекта {i+1}", key=f"project_name_{i}")
            project_link = st.text_input(f"Ссылка на проект {i+1}", key=f"project_link_{i}")
            projects.append({
                "name": project_name,
                "link": project_link
            })

if st.button("Сгенерировать HTML-код", key="generate_button"):
    profile_pic_url = st.image(profile_pic, caption='Фото профиля', use_column_width=True) if profile_pic else ""

    html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Резюме</title>
    <style>
        /* Your CSS styles */
    </style>
</head>
<body>
    <h1>Имя: {name}</h1>
    <p>Электронная почта: {email}</p>
    <p>Телефон: {phone}</p>
    {profile_pic_url}

    <h2>Опыт работы</h2>
    {''.join([f"<p>{job['job_title']} в {job['company']} ({job['start_date']} - {job['end_date']})</p><p>{job['job_description']}</p>" for job in work_experience])}

    <h2>Образование</h2>
    {''.join([f"<p>{school['degree']} по направлению {school['field_of_study']} в {school['school']} ({school['graduation_date']})</p>" for school in education])}

    <h2>Навыки</h2>
    <h3>Профессиональные навыки:</h3>
    <p>{hard_skills}</p>
    <h3>Личные качества:</h3>
    <p>{soft_skills}</p>

    <h2>Проекты</h2>
    {''.join([f"<p>{project['name']} - <a href='{project['link']}' target='_blank'>{project['link']}</a></p>" for project in projects])}
</body>
</html>
    """

    st.code(html_code, language='html')
