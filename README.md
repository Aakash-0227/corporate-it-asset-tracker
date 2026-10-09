# Corporate IT Asset Tracker API

A secure REST API for managing corporate IT assets, built with FastAPI, SQLAlchemy, SQLite, and JWT authentication.

## Features

- User registration and login
- Secure password hashing using Argon2
- JWT access tokens with expiration
- Protected endpoints using bearer-token authentication
- Create, read, update, and delete IT assets
- User-based asset ownership
- Pagination for asset listing
- Request validation using Pydantic
- Interactive API documentation using Swagger UI

## Tech Stack

- **Language:** Python
- **Backend:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Authentication:** JWT
- **Password Hashing:** pwdlib with Argon2
- **Validation:** Pydantic
- **API Documentation:** Swagger UI

## Project Structure

```text
corporate-it-asset-tracker/
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   └── asset_routes.py
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── auth.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or later
- pip
- Git

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aakash-0227/corporate-it-asset-tracker.git
cd corporate-it-asset-tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and replace the placeholder secret with a securely generated random value.

Generate a secret using:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Configure the following variables in `.env`:

```dotenv
SECRET_KEY=your_generated_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./asset_tracker.db
```

Never commit your actual `.env` file or secret key to GitHub.

### 5. Start the API

```bash
uvicorn app.main:app --reload
```

The API runs locally at:

`http://127.0.0.1:8000`

Swagger documentation:

`http://127.0.0.1:8000/docs`

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/register` | Register a user |
| POST | `/auth/login` | Authenticate and obtain a JWT |
| GET | `/auth/me` | Get the authenticated user's details |

### Asset Management

| Method | Endpoint | Description |
|---|---|---|
| POST | `/assets/` | Create an asset |
| GET | `/assets/` | List assets with pagination |
| GET | `/assets/{asset_id}` | Retrieve an asset |
| PUT | `/assets/{asset_id}` | Update an asset |
| DELETE | `/assets/{asset_id}` | Delete an asset |

Asset endpoints require a valid bearer token. Users can access only assets associated with their own account.

## Authentication Workflow

1. Register a user using `/auth/register`.
2. Log in using `/auth/login`. Enter the registered email in the OAuth2 `username` field.
3. Obtain an access token from the response.
4. Authorize in Swagger using the login form.
5. Call protected endpoints using the bearer token.

## Pagination

The asset listing endpoint supports `skip` and `limit` query parameters.

Example:

```text
GET /assets/?skip=0&limit=10
```

## Database

SQLite is used for local development. SQLAlchemy maps Python models to database tables. The application creates the tables during startup.

## Security Notes

- Passwords are hashed before storage.
- JWTs have a configured expiration time.
- Protected routes validate authentication tokens.
- Asset queries enforce user ownership.
- Environment secrets should remain outside version control.

## Author

**Aakash**

GitHub: https://github.com/Aakash-0227
