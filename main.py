import streamlit as st
from PIL import Image
from datetime import datetime

st.set_page_config(page_title="Создатель Резюме", layout="wide")
st.title("Создатель Резюме")

# Личная информация
with st.expander("Личная информация"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Имя")
    with col2:
        email = st.text_input("Электронная почта")
    phone = st.text_input("Телефон")
    profile_pic = st.file_uploader("Загрузить фото профиля", type=["jpg", "jpeg", "png"])

# Опыт работы
with st.expander("Опыт работы"):
    work_experience = []
    num_jobs = st.number_input("Количество мест работы", min_value=1, step=1, value=1)
    for i in range(int(num_jobs)):
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                job_title = st.text_input(f"Должность {i+1}")
            with col2:
                company = st.text_input(f"Компания {i+1}")
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input(f"Дата начала {i+1}")
            with col2:
                end_date = st.date_input(f"Дата окончания {i+1}")
            job_description = st.text_area(f"Описание работы {i+1}", height=100)
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
    num_schools = st.number_input("Количество учебных заведений", min_value=1, step=1, value=1)
    for i in range(int(num_schools)):
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                degree = st.text_input(f"Степень {i+1}")
            with col2:
                field_of_study = st.text_input(f"Направление {i+1}")
            school = st.text_input(f"Учебное заведение {i+1}")
            graduation_date = st.date_input(f"Дата окончания {i+1}")
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
        hard_skills = st.text_area("Профессиональные навыки")
    with col2:
        soft_skills = st.text_area("Личные качества")

# Проекты
with st.expander("Проекты"):
    projects = []
    num_projects = st.number_input("Количество проектов", min_value=0, step=1, value=0)
    for i in range(int(num_projects)):
        with st.container():
            project_name = st.text_input(f"Название проекта {i+1}")
            project_link = st.text_input(f"Ссылка на проект {i+1}")
            projects.append({
                "name": project_name,
                "link": project_link
            })

if st.button("Сгенерировать HTML-код"):
    html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Резюме</title>
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
            display: flex;
            align-items: center;
        }}
        .section h1, .section h2, .section h3 {{
            color: #333;
        }}
        .job-title, .degree, .project-name {{
            font-weight: bold;
        }}
        .job-details, .education-details, .project-link {{
            color: #666;
            margin-bottom: 10px;
        }}
        .profile-pic {{
            margin-right: 20px;
            border-radius: 50%;
            width: 100px;
            height: 100px;
            object-fit: cover;
        }}
    </style>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="section">
            {'<img src="data:image/png;base64,{}" class="profile-pic" />' if profile_pic else ''}
            <div>
                <h1>{name}</h1>
                <p>Электронная почта: {email}</p>
                <p>Телефон: {phone}</p>
            </div>
        </div>

        <div class="section">
            <div>
                <h2>Опыт работы</h2>
                {' '.join([f"""
                <div>
                    <p class="job-title">{job['job_title']} в {job['company']}</p>
                    <p class="job-details">({job['start_date'].strftime('%b %Y')} - {job['end_date'].strftime('%b %Y')})</p>
                    <p>{job['job_description']}</p>
                </div>
                """ for job in work_experience])}
            </div>
        </div>

        <div class="section">
            <div>
                <h2>Образование</h2>
                {' '.join([f"""
                <div>
                    <p class="degree">{school['degree']} по направлению {school['field_of_study']}</p>
                    <p class="education-details">в {school['school']} ({school['graduation_date'].strftime('%b %Y')})</p>
                </div>
                """ for school in education])}
            </div>
        </div>

        <div class="section">
            <div>
                <h2>Навыки</h2>
                <h3>Профессиональные навыки</h3>
                <p>{hard_skills}</p>
                <h3>Личные качества</h3>
                <p>{soft_skills}</p>
            </div>
        </div>

        {f"""
        <div class="section">
            <div>
                <h2>Проекты</h2>
                {' '.join([f"""
                <div>
                    <p class="project-name">{project['name']}</p>
                    <p class="project-link"><a href="{project['link']}" target="_blank">{project['link']}</a></p>
                </div>
                """ for project in projects])}
            </div>
        </div>
        """ if projects else ""}
    </div>
</body>
</html>
    """

    st.code(html_code, language='html')
