# Task Todo API

A simple REST API for managing tasks, built with Flask and PostgreSQL.

## Tech Stack

- **Web Framework:** Flask
- **Database:** PostgreSQL
- **ORM:** Flask-SQLAlchemy
- **Migrations:** Flask-Migrate (Alembic)
- **Environment Management:** python-dotenv

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- PostgreSQL
- Git

### 2. Configure Environment
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with the following content (adjust values for your database):
   ```ini
   SECRET_KEY=your database secret key
   FLASK_ENV=development
   FLASK_DEBUG=True
   
   # Database Configuration

   DATABASE_URL=postgresql://your_database_user:your_database_password@localhost:5432/your_database_name
   ```

### 3. Initialize and Migrate the Database
Initialize and migrate the database:
```bash
flask db init      # If not already initialized
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Run the Application
Start the development server:
```bash
python run.py
```
The API will be available at `http://localhost:8000`.

---

## API Documentation & Testing

You can test the API using Postman, curl, or any HTTP client.

### Base URL: `http://localhost:8000/api/tasks`

### 1. Create a Task (POST)
**Endpoint:** `/`
**Body:** JSON
```json
{
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs"
}
```
**Curl Example:**
```bash
curl -X POST http://localhost:8000/api/tasks/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Buy groceries", "description": "Milk, Bread, Eggs"}'
```

### 2. Get All Tasks (GET)
**Endpoint:** `/`
**Query Params:**
- `page` (int): Page number (default: 1)
- `per_page` (int): Items per page (default: 10)
- `completed` (true/false): Filter by completion status
- `sort` (str): Field to sort by (default: created_at)
- `order` (asc/desc): Sort order (default: desc)

**Curl Example:**
```bash
curl "http://localhost:8000/api/tasks/?page=1&per_page=5"
```

### 3. Get Single Task (GET)
**Endpoint:** `/<task_id>`

**Curl Example:**
```bash
curl http://localhost:8000/api/tasks/1
```

### 4. Update Task (PUT)
**Endpoint:** `/<task_id>`
**Body:** JSON (Partial updates allowed)
```json
{
  "is_completed": true
}
```
**Curl Example:**
```bash
curl -X PUT http://localhost:8000/api/tasks/1 \
     -H "Content-Type: application/json" \
     -d '{"is_completed": true}'
```

### 5. Delete Task (DELETE)
**Endpoint:** `/<task_id>`

**Curl Example:**
```bash
curl -X DELETE http://localhost:8000/api/tasks/1
```
