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
**Description:** Retrieve a list of tasks.

**Curl Example:**
```bash
curl "http://localhost:8000/api/tasks/"
```

### 3. Filtering
**Endpoint:** `/`
**Query Param:** `completed` (true/false)

Filter tasks by their completion status.

**Example: Get only completed tasks**
```bash
curl "http://localhost:8000/api/tasks/?completed=true"
```
**Example: Get only pending tasks**
```bash
curl "http://localhost:8000/api/tasks/?completed=false"
```

### 4. Sorting
**Endpoint:** `/`
**Query Params:**
- `sort`: Field to sort by (e.g., `created_at`, `title`). Default: `created_at`.
- `order`: Sort direction (`asc` or `desc`). Default: `desc`.

**Example: Sort by title in ascending order**
```bash
curl "http://localhost:8000/api/tasks/?sort=title&order=asc"
```

### 5. Pagination
**Endpoint:** `/`
**Query Params:**
- `page`: Page number. Default: 1.
- `per_page`: Number of items per page. Default: 10.

**Response Structure:**
The response includes metadata (`total`, `pages`, `page`) along with the `tasks` list.

**Example: Get page 2 with 5 tasks per page**
```bash
curl "http://localhost:8000/api/tasks/?page=2&per_page=5"
```

### 6. Get Single Task (GET)
**Endpoint:** `/<task_id>`

**Curl Example:**
```bash
curl http://localhost:8000/api/tasks/1
```

### 7. Update Task (PUT)
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

### 8. Delete Task (DELETE)
**Endpoint:** `/<task_id>`

**Curl Example:**
```bash
curl -X DELETE http://localhost:8000/api/tasks/1
```
