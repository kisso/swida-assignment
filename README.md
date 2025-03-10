# Swida assignment

This repository contains both the backend and frontend applications for the project. The backend is built with Django, and the frontend is developed using Vue 3.

## Project Structure

```
project-root/
│-- backend/  # Django Backend
│-- frontend/  # Vue 3 Frontend
│-- README.md
```

---

## Installation & Setup

### 1. Backend (Django)

#### Prerequisites:
- Python (>=3.11)
- Poetry (==1.8.4)
- Virtual environment tool

#### Setup:
```sh
cd backend
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate virtual environment
poetry install  # Install dependencies or pip install -r requirements.txt
python manage.py migrate  # Apply migrations
python manage.py loaddata order_fixture.json waypoint_fixture.json # Load fixtures
python manage.py runserver  # Run server
```

### 2. Frontend (Vue 3)

#### Prerequisites:
- Node (>=22.0)
- npm

#### Setup:
```sh
cd frontend
npm install  # Install dependencies
cp .env.example .env
npm run dev  # Start development server
```

#### Environment Variables
Create a `.env` file in the `frontend/` directory:
```
VITE_API_URL=http://localhost:8000/api/v1/
```

---

## Running the Full Application
1. Start the Django backend: `cd backend && python manage.py runserver`
2. Start the Vue frontend: `cd frontend && npm run dev`

The frontend will run on `http://localhost:5173/` (Vite default), and the backend API will be available at `http://localhost:8000/`.
