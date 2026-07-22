# 🔐 Encrypted CLI Password Vault

> A modular command-line password manager written in Python.
>
> This project was created as a learning project to improve my software engineering, Python, database, testing, and application architecture skills.

---

## 📖 About

The **Encrypted CLI Password Vault** is a command-line application that allows users to securely store credentials in a local SQLite database.

The main goal of this project is **not only to build a password manager**, but also to learn how professional Python applications are designed and structured.

Throughout this project I focus on:

- Clean Architecture
- Modular Design
- Separation of Responsibilities
- Unit Testing
- Error Handling
- Secure Password Storage
- Database Design
- Version Control (Git)

---

## ✨ Current Features

### Authentication

- User Registration
- Secure Login
- Password hashing using **bcrypt**
- Email validation
- Password validation
- Duplicate account prevention

### Database

- SQLite database
- Automatic database creation
- Automatic table creation
- Modular storage layer

### Architecture

- Modular application design
- Separate business logic
- Storage abstraction layer
- Custom exceptions
- Rich CLI interface

### Testing

- Unit tests using **pytest**
- Mocking
- Exception testing
- Database testing

---

## 🚧 Planned Features

- [x] Login System
- [x] Registration
- [x] Database Layer
- [x] Storage Logic Layer
- [x] Unit Testing
- [x] Git Integration

### Password Vault

- [ ] Add Credential
- [ ] View Credentials
- [ ] Search Credentials
- [ ] Edit Credential
- [ ] Delete Credential
- [ ] Credential Encryption
- [ ] Pagination
- [ ] Export Functionality

---

## 🏗️ Project Structure

```text
Encrypted_CLI_Password_Vault
│
├── src/
│   ├── cli.py
│   ├── crypto.py
│   ├── error.py
│   ├── login_logic.py
│   ├── main.py
│   ├── main_logic.py
│   ├── storage.py
│   ├── storage_logic.py
│   ├── validator.py
│   ├── vault_logic.py
│   └── vault_services/
│
├── tests/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🛠 Technologies

- Python 3.14
- SQLite3
- Rich
- bcrypt
- pytest
- Git

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Timeless101/Encrypted-CLI-password-vault.git
```

Navigate into the project

```bash
cd Encrypted-CLI-password-vault
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m src.main
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📚 What I Learned

This project has helped me learn:

- Python application architecture
- Separation of concerns
- SQLite database design
- Exception handling
- Unit testing with pytest
- Git & GitHub
- Modular programming
- Refactoring large applications
- Building maintainable software

---

## 🎯 Future Goals

After completing the CLI version, I plan to continue developing this project by creating:

- REST API (FastAPI)
- Web Interface
- Multi-user Authentication
- Docker Deployment
- PostgreSQL Support
- Cloud Deployment

---

## 📄 License

This project is created for educational purposes.

---

## 👨‍💻 Author

**Diego Wuck**

System Engineer • Python Enthusiast • Future Cloud Architect
