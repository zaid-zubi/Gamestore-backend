# Backend Setup Guide

## 📦 Prerequisites

* Python 3.12+
* Poetry installed
* PostgreSQL running locally

---

## 🗄️ Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE game_store;
```

---

## ⚙️ Environment Variables

Create a `.env` file in the backend root directory:

```env
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=game_store
JWT_SECRET_KEY=
```

> 🔐 Make sure to generate a secure JWT secret key before running the application.
> Use command bellow:
```commandline
python -c "import secrets; print(secrets.token_hex(32))"
```
---

## 📥 Install Dependencies

```bash
make install
```

---

## 🐍 Activate Virtual Environment (Poetry)

```bash
make activate
```

---

## 📊 Import CSV Data

This will load game items from the CSV file into the database:

```bash
make import-csv
```

---

## 👤 Create Default Admin User

This will seed an initial admin account:

```bash
make default-admin
```

---

If you're not using Alembic, ignore this suggestion.

---

### 4. Mention the default admin credentials
Since you're creating a default admin, reviewers need to know how to log in.

```md
## 🔑 Default Admin Credentials

Email: admin@example.com
Password: admin123
```
## 🚀 Run the Backend Server

```bash
make run
```

## Open Swagger docs
```commandline
http://127.0.0.1:8000/docs
```
---# Gamestore-backend

## Testing APIs
```commandline
export PYTHONPATH=.
pytest
```