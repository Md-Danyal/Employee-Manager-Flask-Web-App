<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=30&duration=3000&pause=1000&color=4F86F7&center=true&vCenter=true&width=600&lines=Employee+Manager+System;Built+with+Flask+%2B+MySQL;Full+CRUD+Operations" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-Template-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge&logo=css3&logoColor=white)

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange?style=flat-square)

<br/>

> **A full-stack Employee Management System** built with Python Flask, SQLAlchemy ORM, and MySQL — featuring complete CRUD operations with a clean, responsive UI.

<br/>

[🚀 Features](#-features) • [🛠 Tech Stack](#-tech-stack) • [⚡ Quick Start](#-quick-start) • [📁 Project Structure](#-project-structure) • [📸 Screenshots](#-screenshots) • [🤝 Contributing](#-contributing)

</div>

---

## 📸 Screenshots

<!-- > *(Add your app screenshots here — Home page, Add Employee form, Employee list, Edit page)* -->

| Home / Dashboard | Add Employee |
|:-:|:-:|
| `---------------` | ![Add Employee](screenshots/add_employees.png) |

| Employee List | Edit Employee |
|:-:|:-:|
| ![View Employees](screenshots/View_employees.png) | ![Edit Employee](screenshots/Edit_employees.png) |

---

## 🚀 Features

- ✅ **Create** — Add new employees with name, department, role, and salary details
- 📋 **Read** — View all employees in a clean, organized table
- ✏️ **Update** — Edit any employee record instantly
- 🗑️ **Delete** — Remove employee records with confirmation
- 💾 **MySQL Database** — Persistent storage via SQLAlchemy ORM
- 🎨 **Clean UI** — Responsive design built with Jinja2 + CSS

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3, Flask |
| **Frontend** | Jinja2 Templates, CSS3 |
| **ORM** | SQLAlchemy |
| **Database** | MySQL (via MySQL Connector) |
| **Server** | Flask Development Server |

---

## 📁 Project Structure

```
employee-manager/
│
├── main.py                  # Main Flask application & routes
├── db/
|   ├── __init__.py
|   ├── db_pool.py          # SQLALchemy and MySql+Connector+Python
|   ├── models.py           # SQLAlchemy Employee model
|   ├── repository.py       # SQLAlchemy Queries
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── .gitignore
│
├── templates/              # Jinja2 HTML templates
│   ├── base.html           # Base layout template
│   ├── home.html           # Add employee form
│   ├── views_employees.html# Employee list page
│   └── view_emp.html       # Edit employee data
│
└── static/
    └── css/
        └── style.css       # Custom stylesheet
```

---

## ⚡ Quick Start

### Prerequisites

Make sure you have the following installed:
- Python 3.8+
- MySQL Server
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Md-Danyal/Employee-Manager-Flask-Web-App
cd employee-manager
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

```sql
-- Run in MySQL
CREATE DATABASE employee_db;
```

### 5. Configure environment variables

Create a `.env` file in the root directory:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=employee_db
SECRET_KEY=your-secret-key-here
```

### 6. Run the app

```bash
python main.py
```

Visit 👉 `http://127.0.0.1:5000`

---

## 🔧 CRUD Operations

| Operation | Route | Method | Description |
|-----------|-------|--------|-------------|
| Read all | `/` | GET | View all employees |
| Create | `/add` | GET, POST | Add new employee |
| Update | `/edit/<id>` | GET, POST | Edit employee |
| Delete | `/delete/<id>` | POST | Remove employee |

---

## 📦 Requirements

```txt
Flask
Flask-SQLAlchemy
mysql-connector-python
python-dotenv
```

Generate with:
```bash
pip freeze > requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by Md-Danyal using Python & Flask

⭐ **Star this repo if you found it helpful!** ⭐

</div>
