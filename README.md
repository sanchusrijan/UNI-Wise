# 🎓 UNI-Wise  
### A Web Solution for Students

UNI-Wise is a student-focused web platform designed to organize academic tools and resources in one place. The goal is to simplify student workflows and improve productivity through a clean, minimal, and scalable web application.

---

## 🚀 Current Features

- 📊 **Student Dashboard** – Centralized view of student-related tools  
- 📝 **Notes & Resource Management** – Upload and organize academic content  
- 📅 **Task & Deadline Tracking** – Keep track of assignments and schedules  
- 🎨 **Modern UI** – Clean, responsive, and student-friendly interface  
- 🔐 **Secure Backend** – Built with scalability and best practices in mind  

---

## 🛠️ Tech Stack

**Frontend**
- HTML, CSS, JavaScript  

**Backend**
- Django  
- Django REST Framework  

**Database**
- PostgreSQL / SQLite  

**Tools**
- Git & GitHub  

---

## 🚀 Current Features

- 👤 **User Management**
  - User authentication and profile handling
  - Secure backend using Django best practices

- 📂 **Document Management**
  - Store and manage academic documents
  - Structured handling of student resources

- 🎨 **Frontend Integration**
  - HTML templates with static assets
  - Clean and responsive UI design

- ⚙️ **Backend Architecture**
  - Modular Django apps
  - SQLite database for development

---

## 📂 Project Structure

> The project follows a custom structure based on development needs.  
> Please refer to the repository files for the exact layout.
>
```text
> UNI-WISE/
│── .venv/              # Virtual environment
│── .vscode/            # Editor configuration
│── documents/          # Document-related app/resources
│── static/             # Static files (CSS, JS, assets)
│── summarize/          # Summarization module (future development)
│── template/           # HTML templates
│── UNI_Wise/           # Main Django project settings
│── users/              # User management app
│── db.sqlite3          # Development database
│── manage.py           # Django entry point
│── requirements.txt    # Project dependencies

---
```

## ⚙️ Setup & Installation

1. Clone the repository:
```bash
git clone https://github.com/sanchusrijan/UNI-Wise.git
cd UNI-Wise
```

2. Create and activate virtual environment:
 ```bash
   python3 -m venv .venv
   source .venv/bin/activate
```

3.Install dependencies:
```bash
  pip3 install -r requirements.txt
```
4.Run migrations:
```bash
python manage.py migrate
```

5.Start the development server:
```bash
python manage.py runserver
```

6.Open in browser:
  ```bash
  http://127.0.0.1:8000/accounts/
  ```

