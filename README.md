# Swida assignment

This repository contains both the backend and frontend applications for the project. The backend is built with Django, and the frontend is developed using Vue 3.

# Assumptions & Decisions

I used an SQLite database for simplicity, but for production, I would definitely choose PostgreSQL. Additionally, I used Poetry for dependency management. I implemented the API using Django and the django-api-forms library, which is used for creating and validating forms. I also used the django-filter library to create basic filters. 

In a production, I would definitely focus on security, where I would implement an API keys validation and ensure data integrity with signing the requests, also I would introduce users with permissions.

On the frontend, I used a stack that I typically use for developing React apps, which includes Axios, useQuery, and Tailwind CSS. I like useQuery for simplicity of usage. When adding/deleting orders I just invalidate queries and useQuery will automatically fetch new data, it is store for the application.

## Approach for business case

I created the entities Order and Waypoint, which have one-to-many relation. For orders, I added an auto-increment field called order_number, so the user does not have to enter it manually, ensuring consistency.

I also added sequence field for Waypoint to track sequence for driver. In future versions I would implmement feature for reordering and setting date for each waypoint.

For each entity, I added a created_at field to track the creation time of entries. Additionally, I included a deleted_at field, which is set when an object is deleted. Once deleted, the object will no longer be returned in query results but will remain in the database. This allows us to retain data for a certain period (e.g., 30 days) in case it needs to be restored. I would set up a cron job to automatically hard delete expired objects. This ensures that after the retention period (e.g., 30 days), deleted records are permanently removed from the database.

In the listing orders API request, I also return the waypoints for each order. For scaled application I would introduce pagination.

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
cp .env.example .env # Create .env file
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
