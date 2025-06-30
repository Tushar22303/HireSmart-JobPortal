# 🧑‍💼 Job Portal Web App (Django + MySQL)

A full-featured **Job Portal** web application built with **Django**, featuring role-based dashboards for **Job Seekers** and **Employers**, resume uploads, job applications, and profile management.

Ideal for beginner to intermediate developers looking to showcase real-world Django development skills.

---

## 🔧 Features

### 👨‍💻 Job Seekers

- Register & login with role-based access
- Upload and update resume (PDF)
- Upload and update profile picture
- View job listings and details
- Apply for jobs
- View applied jobs

### 🏢 Employers (Admins)

- Register & login as an Employer
- Post new jobs
- View list of posted jobs
- View applicants for each job

### 🌐 General

- MySQL database integration
- Role-based dynamic dashboards
- Secure file uploads (media storage)
- Fully modular Django project structure
- CLI & template-based UI structure
- .env configuration for security

---

## 🛠️ Tech Stack

---

| Layer        | Technology                       |
| ------------ | -------------------------------- |
| Backend      | Django (Python)                  |
| Database     | MySQL                            |
| Frontend     | HTML, CSS (Basic)                |
| Auth System  | Django Auth + Custom UserProfile |
| File Uploads | Django Media                     |
| Env Manager  | python-decouple                  |

---

---

<!-- ------------------------------------------------------- -->

## 🚀 Project Structure

jobportal_project/
│
├── manage.py
├── .env
├── requirements.txt
├── .venv/
│
│
├── jobportal_project/ ← Core settings and URLs
├── accounts/ <- app -> register, login, logout, etc...
├── core/ <- app -> home page, about page, etc...
├── jobs/ <- app -> job_list, post_job, job_detail, apply_job, etc...
│
├── media/ ← Uploaded resumes, profile images
├── static/ ← Optional static files (CSS/JS)
├── templates/ ← Base and shared HTML templates

---

<!-- ------------------------------------------------------- -->

# Media Configuration and Static Configuration

# Static files

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

<!-- ------------------------------------------------------- -->

## 🧪 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/jobportal_project.git
cd jobportal_project
```

<!-- ------------------------------------------------------- -->

# Virtual Environment

python -m venv .venv

# On Mac:

source env/bin/activate

# On Windows:

.venv\Scripts\activate

<!-- ------------------------------------------------------- -->

# requirements.txt

pip install -r requirements.txt

<!-- ------------------------------------------------------- -->

# Configure MYSQL Database

DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=jobportal_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306

<!-- ------------------------------------------------------- -->

# run migrations

python manage.py makemigrations
python manage.py migrate

<!-- ------------------------------------------------------- -->

# create superuser

python manage.py createsuperuser

<!-- ------------------------------------------------------- -->

# run server

python manage.py runserver
