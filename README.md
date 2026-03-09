# Vaultx-Encrypted-Vault-SAAS-APP

> A secure, modern password vault web application built with Django and Fernet cryptography.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?style=flat-square&logo=django)
![Cryptography](https://img.shields.io/badge/Encryption-Fernet%20AES--128-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🌐 Live Demo

> **[YOUR-APP-NAME.onrender.com](https://your-app-name.onrender.com)**  
> *(Replace with your actual Render URL)*

---

## 📌 About VaultX

VaultX is a SaaS-style password vault prototype that allows users to securely store, manage, and retrieve login credentials for multiple websites and services.

All sensitive data — usernames, passwords, and notes — is **encrypted using Fernet symmetric encryption (AES-128-CBC + HMAC-SHA256)** before being stored in the database. This means even if the database is compromised, stored credentials remain completely unreadable without the secret key.

This project was built as part of the topic:
**"Secure Login and Authentication by Cryptography"**

---

## ✨ Features

- 🔐 **Fernet Encryption** — All credentials encrypted before database storage
- 👤 **User Authentication** — Register, login, logout using Django's built-in auth system
- 🗄️ **Credential Vault** — Add, view, edit, delete stored credentials
- 👁️ **Reveal Password** — Toggle password visibility per vault item
- 📋 **Copy to Clipboard** — One-click password copy
- 📎 **File Attachments** — Attach PDF, DOC, XLSX, JPG, PNG, MP4 to vault items
- 💪 **Password Strength Indicator** — Live strength meter on password fields
- 🎨 **Glassmorphism UI** — Modern dark-glass login/register design
- 📱 **Responsive Layout** — Works on desktop and mobile

---

## 🛡️ How Encryption Works

```
User enters password
        ↓
set_password(raw) called
        ↓
Fernet(key).encrypt(password.encode())
        ↓
Encrypted bytes stored in database
        ↓
get_password() called on retrieval
        ↓
Fernet(key).decrypt(encrypted_bytes)
        ↓
Original password returned to user
```

The encryption key is derived from Django's `SECRET_KEY` using SHA-256 hashing, then base64-encoded to meet Fernet's key format requirement.

---

## 🧰 Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.12, Django 6.0 |
| Encryption | `cryptography` library — Fernet (AES-128-CBC + HMAC-SHA256) |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite (prototype) |
| Fonts | Syne, DM Sans (Google Fonts) |
| Icons | Heroicons (inline SVG) |
| Deployment | Render, Gunicorn, WhiteNoise |

---

## 📁 Project Structure

```
vaultx/
├── accounts/               # User authentication app
│   ├── forms.py            # Register form
│   ├── views.py            # Login, register, logout views
│   └── urls.py
├── vault/                  # Vault management app
│   ├── models.py           # VaultItem, VaultFile models with encryption
│   ├── views.py            # Dashboard, add, edit, delete views
│   └── urls.py
├── config/                 # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/              # HTML templates
│   ├── base.html
│   ├── auth_base.html
│   ├── developer.html
│   ├── account/
│   │   ├── login.html
│   │   └── register.html
│   └── vault/
│       ├── dashboard.html
│       ├── add_item.html
│       ├── edit_item.html
├── static/
│   ├── css/style.css
│   └── images/
├── build.sh                # Render build script
├── requirements.txt
└── manage.py
```

---

## 🚀 Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/Niramaynextgen/Vaultx-Encrypted-Vault-SAAS-APP.git
cd Vaultx-Encrypted-Vault-SAAS-APP
```

**2. Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create `.env` file**
```bash
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost
```

**5. Run migrations**
```bash
python manage.py migrate
```

**6. Start server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key — used to derive encryption key |
| `DEBUG` | `True` for development, `False` for production |
| `ALLOWED_HOSTS` | Comma-separated allowed hostnames |

---

## 📚 References

| Resource | Link |
|---|---|
| Python Fernet Encryption | https://cryptography.io/en/latest/fernet/ |
| Django Documentation | https://docs.djangoproject.com |
| Heroicons | https://heroicons.com |
| Google Fonts — Syne | https://fonts.google.com/specimen/Syne |
| Google Fonts — DM Sans | https://fonts.google.com/specimen/DM+Sans |
| Glassmorphism CSS | https://css.glass |

---

## 👨‍💻 Developer

**Niramay Shrivastava**  
Backend Developer  
GitHub: [@Niramaynextgen](https://github.com/Niramaynextgen)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
