# Task Management API

A robust RESTful API built with Django and Django REST Framework for managing tasks. This project implements a complete task management system with search, filter, and sorting capabilities.

## Features
- Full CRUD operations for tasks
- Search functionality by task title
- Date-based filtering
- Custom sorting options
- Pagination support
- RESTful API design

## Technology Stack
- Python 3.8+
- Django 4.2.1
- Django REST Framework 3.14.0
- SQLite (default database)
- Docker & Docker Compose (optional)

## Installation & Setup

You can run this project either using Docker or traditional local setup.

### Option 1: Docker Setup (Recommended)

#### Prerequisites
- Docker
- Docker Compose

#### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd django-tasks-assignment
   ```

2. Build and run the containers:
   ```bash
   docker-compose up --build
   ```

3. The API will be available at `http://localhost:8000`

#### Useful Docker Commands
```bash
# Stop the containers
docker-compose down

# View logs
docker-compose logs

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

### Option 2: Local Setup

#### Prerequisites
- Python 3.8+
- pip (Python package manager)

#### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd django-tasks-assignment
   ```

2. Create and activate virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate on Windows
   venv\Scripts\activate
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Documentation

### Base URL
All API requests are made to: `http://localhost:8000/`

### Endpoints

#### 1. Create Task
```http
POST /tasks/
Content-Type: application/json

{
    "title": "Internship backend",
    "description": "This is a django internship "
}
```

#### 2. List Tasks
```http
GET /tasks/                   # List all tasks
GET /tasks/?search=intern   # Search by title
GET /tasks/?search_date=2024-05-03  # Filter by date
GET /tasks/?sort_by_date=true       # Sort by date
```

#### 3. Update Task
```http
PATCH /tasks/{id}/
Content-Type: application/json

{
    "title": "Updated full stack",
    "description": "Updated description"
}
```

#### 4. Delete Task
```http
DELETE /tasks/{id}/
```

### Response Examples

#### Successful Task Creation (201 Created)
```json
{
    "id": 1,
    "title": "backend internship",
    "description": "This is a django internship",
    "created_at": "2024-05-03T10:30:00Z",
    "updated_at": "2024-05-03T10:30:00Z"
}
```

#### Task List (200 OK)
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "backend internship",
            "description": "This is a django internship",
            "created_at": "2024-05-03T10:30:00Z",
            "updated_at": "2024-05-03T10:30:00Z"
        }
    ]
}
```

## Testing the API

### Using cURL
```bash
# Create a task
curl -X POST http://localhost:8000/tasks/ \
     -H "Content-Type: application/json" \
     -d '{
         "title": "Test API",
         "description": "Verify API functionality"
     }'

# List tasks
curl http://localhost:8000/tasks/

# Update task
curl -X PATCH http://localhost:8000/tasks/1/ \
     -H "Content-Type: application/json" \
     -d '{
         "title": "Updated task"
     }'

# Delete task
curl -X DELETE http://localhost:8000/tasks/1/
```

### Using Postman
1. Import the provided Postman collection (if available)
2. Or create new requests using the endpoints documented above
3. Set Content-Type header to `application/json` for POST/PATCH requests

## Project Structure
```
django-tasks-assignment/
├── core/                 # Project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL routing
│   └── wsgi.py          # WSGI configuration
├── tasks/               # Task management app
│   ├── models.py        # Data models
│   ├── serializers.py   # API serializers
│   ├── views.py         # API views
│   └── urls.py          # API routing
├── manage.py            # Django management
├── requirements.txt     # Python dependencies
└── docker-compose.yml   # Docker configuration
```

## Error Handling

### Status Codes
- 200: Successful GET/PATCH
- 201: Successful POST
- 204: Successful DELETE
- 400: Bad Request
- 404: Not Found
- 500: Server Error

### Error Response Format
```json
{
    "detail": "Error message"
}
```

## Development Notes

### Important Considerations
- Tasks are paginated (10 items per page)
- Dates should be in YYYY-MM-DD format
- Task descriptions are optional
- Default sorting is by creation date (newest first)

### Common Issues
1. **Module Import Errors**
   - Verify virtual environment is activated
   - Confirm all dependencies are installed

2. **Database Issues**
   - Run `python manage.py makemigrations`
   - Apply migrations with `python manage.py migrate`

3. **Port Conflicts**
   - Change port: `python manage.py runserver 8001`
   - Or stop conflicting services





## License
This project is licensed under the MIT License - see the LICENSE file for details.
