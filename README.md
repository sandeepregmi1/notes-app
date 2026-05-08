# Notes API 🚀

A robust backend for a Notes application built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. This project implements secure user authentication and personalized note management.

---

## 🌟 Phase 1 Features

- [x] **User Authentication**: Secure Login/Registration using JWT (JSON Web Tokens).
- [x] **Create Notes**: Users can create their own notes.
- [x] **Retrieve Notes**: Users can fetch their own notes with support for **Pagination**.
- [x] **Database Integration**: PostgreSQL integration with SQLAlchemy ORM.
- [x] **Environment Security**: Sensitive data managed via environment variables.

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Database**: PostgreSQL
- **Security**: OAuth2 with Password hashing (Bcrypt) & JWT
- **Validation**: Pydantic

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd notes_app
```

### 2. Set up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and copy the contents from `.env.example`, then fill in your actual credentials.
```bash
cp .env.example .env
```

### 5. Run the Application
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.
You can access the interactive Swagger documentation at `http://127.0.0.1:8000/docs`.

---

## 📈 Roadmap (Phase 2 & Beyond)
- [ ] Update and Delete functionality for notes.
- [ ] Search and Filter notes by title or content.
- [ ] User Profile management.
- [ ] Unit and Integration tests.
- [ ] Dockerization for easy deployment.

---

## 📄 License
This project is licensed under the MIT License.
