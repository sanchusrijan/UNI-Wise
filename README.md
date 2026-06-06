# 🎓 UNI-Wise  
### A Web Solution for Students

UNI-Wise is a student-focused web platform designed to organize academic tools and resources in one place. The goal is to simplify student workflows and improve productivity through a clean, minimal, and scalable web application.

---

## 🚀 Current Features

- 👤 **User Management**
  - User authentication and registration handling
  - Secure token-based session management using Django REST Framework and JWT
- 📂 **Document Management**
  - Secure storage and handling of academic resources (PDF files)
  - Automatic on-demand text extraction using `pdfplumber`
- 🧠 **AI-Driven Summarization**
  - Multi-stage chunked summarization using Hugging Face's pre-trained BART-large-cnn model
  - Automatic sentence and phrase deduplication to optimize summary quality
- 🎨 **Responsive UI**
  - Clean, modern, and student-friendly HTML templates with vanilla CSS styling
  - Dynamic drag-and-drop document uploading and document sidebar list

---

## 🚧 In Development (Future Scope)

- 📊 **Student Dashboard** – Centralized view of student-related tools and summaries
- 📝 **Notes & Study Management** – Create, organize, and search study guides and notes
- 📅 **Task & Deadline Tracking** – Keep track of assignments, schedules, and exam dates
- 🖼️ **Image Processing** – Scanned note uploading and image-to-text processing
- 🧪 **Quiz Generation** – Automatic quiz creation from uploaded study guides for self-assessment

---

## 🛠️ Tech Stack

**Frontend**
- HTML, Vanilla CSS, JavaScript  

**Backend**
- Django  
- Django REST Framework  
- Hugging Face Transformers (BART Model)

**Database**
- PostgreSQL (Primary) / SQLite (Backup)

---

## 📂 Project Structure

> The project follows a custom structure based on development needs.  
> Please refer to the repository files for the exact layout.

```text
UNI-WISE/
│── .venv/              # Virtual environment
│── .vscode/            # Editor configuration
│── documents/          # Document-related app/resources
│── static/             # Static files (CSS, JS, assets)
│── summarize/          # Summarization module (AI service)
│── template/           # HTML templates
│── UNI_Wise/           # Main Django project settings
│── users/              # User management app
│── db.sqlite3          # Development database
│── manage.py           # Django entry point
│── requirements.txt    # Project dependencies
```

---

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

3. Install dependencies:
```bash
pip3 install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Open in browser:
```bash
http://127.0.0.1:8000/accounts/login/
```

