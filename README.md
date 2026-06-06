# 🎓 UNI-Wise  
### A Web Solution for Students

UNI-Wise is a student-focused web platform designed to organize academic tools and resources in one place. The goal is to simplify student workflows and improve productivity through a clean, minimal, and scalable web application.

# ✅✅✅✅✅✅ Pls review the setup given below to try the website for ur self.✅✅✅✅✅✅✅

---

## 🚧 Project Status

UNI-Wise is **currently under active development** and is **not yet finished**.  
Several advanced features are in progress and will be added in future updates.

---

## 🔮 Features Under Development

- 🧠 **Advanced AI Summarization**
  - NLP-based summarization of notes and documents
  - Extraction of key points and highlights

- 🖼️ **Image Processing**
  - Processing images from study materials
  - Support for scanned notes and visual content

- 🧪 **Quiz Generation**
  - Automatic quiz creation from notes and documents
  - Question generation for self-assessment and revision

- 📊 **Smart Study Tools**
  - Personalized learning assistance
  - Intelligent content recommendations

---

## 🎯 Development Note

The current version focuses on building a **strong, scalable foundation**.  
Advanced AI-driven features are being developed incrementally and will be integrated once stable.

---

## 🚀 Current Features

- 🔐 **Authentication**
  - User login and signup system
  - Secure access to personalized features

- 🏠 **Home Page**
  - Central landing page for authenticated users
  - Easy navigation to different modules

- 🧠 **Summarizer (Base Structure)**
  - Dedicated summarizer module
  - UI and backend structure in place for future AI-based summarization
  - Currently supports text submission and request handling

- 📂 **Files Tab**
  - Separate section to view uploaded files
  - Organized display of user documents and resources

- ⬆️ **File Upload Feature**
  - Users can upload files for storage and future processing
  - Integrated with backend for document handling
 
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

6.Open in browser ( RECOMENDED : Google Chrome ):
  ```bash
  http://127.0.0.1:8000/accounts/
  ```

