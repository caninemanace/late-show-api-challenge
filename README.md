# Late Night TV Show API

A Flask REST API for managing a Late Night TV show system with guests, episodes, and appearances. Built with MVC architecture, PostgreSQL database, and JWT authentication.

## Features

- **MVC Architecture**: Clean separation of concerns with models, views, and controllers
- **PostgreSQL Database**: Robust relational database with proper relationships
- **JWT Authentication**: Secure token-based authentication for protected routes
- **RESTful API**: Well-structured REST endpoints following best practices
- **Data Validation**: Input validation and error handling
- **Cascade Deletes**: Proper foreign key relationships with cascade operations

## Models

### User
- `id` - Primary key
- `username` - Unique username
- `password_hash` - Hashed password for security

### Guest
- `id` - Primary key
- `name` - Guest's full name
- `occupation` - Guest's profession

### Episode
- `id` - Primary key
- `date` - Episode air date
- `number` - Unique episode number

### Appearance
- `id` - Primary key
- `rating` - Performance rating (1-5, validated)
- `guest_id` - Foreign key to Guest
- `episode_id` - Foreign key to Episode

## 🛠 Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL
- pipenv

### 1. Clone Repository
```bash
git clone https://github.com/caninemanace/late-show-api-challenge.git
cd late-show-api-challenge
```

### 2. Install Dependencies
```bash
pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary pipenv shell
```

### 3. PostgreSQL Setup
Create your database in PostgreSQL:
```sql
CREATE DATABASE late_show_db;
```

### 4. Configure Environment
Update the database URI in `server/config.py`:
```python
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/late_show_db"
```

### 5. Database Migration
```bash
export FLASK_APP=server/app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 6. Seed Database
```bash
python server/seed.py
```

### 7. Run Application
```bash
python server/app.py
```

The API will be available at `http://localhost:5000`

##  Authentication Flow

### 1. Register a User
```bash
POST /register
{
    "username": "your_username",
    "password": "your_password"
}
```

### 2. Login to Get JWT Token
```bash
POST /login
{
    "username": "your_username",
    "password": "your_password"
}
```

### 3. Use Token in Protected Routes
Include the token in the Authorization header:
```
Authorization: Bearer <your_jwt_token>
```

##  API Routes

| Route | Method | Auth Required? | Description |
|-------|--------|----------------|-------------|
| `/register` | POST | ❌ | Register a new user |
| `/login` | POST | ❌ | Login and get JWT token |
| `/episodes` | GET | ❌ | Get all episodes |
| `/episodes/<int:id>` | GET | ❌ | Get specific episode with appearances |
| `/episodes/<int:id>` | DELETE | ✅ | Delete episode (cascades to appearances) |
| `/guests` | GET | ❌ | Get all guests |
| `/appearances` | POST | ✅ | Create new appearance |

##  API Examples

### Register User
```bash
POST /register
Content-Type: application/json

{
    "username": "newuser",
    "password": "password123"
}
```

**Response:**
```json
{
    "message": "User registered successfully",
    "user": {
        "id": 1,
        "username": "newuser"
    }
}
```

### Login
```bash
POST /login
Content-Type: application/json

{
    "username": "admin",
    "password": "password123"
}
```

**Response:**
```json
{
    "message": "Login successful",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "user": {
        "id": 1,
        "username": "admin"
    }
}
```

### Get All Episodes
```bash
GET /episodes
```

**Response:**
```json
{
    "episodes": [
        {
            "id": 1,
            "date": "2024-01-15",
            "number": 101
        }
    ]
}
```

### Get Episode with Appearances
```bash
GET /episodes/1
```

**Response:**
```json
{
    "episode": {
        "id": 1,
        "date": "2024-01-15",
        "number": 101,
        "appearances": [
            {
                "id": 1,
                "rating": 5,
                "guest_id": 1,
                "episode_id": 1,
                "guest": {
                    "id": 1,
                    "name": "Jennifer Lawrence",
                    "occupation": "Actress"
                }
            }
        ]
    }
}
```

### Create Appearance (Auth Required)
```bash
POST /appearances
Authorization: Bearer <token>
Content-Type: application/json

{
    "rating": 4,
    "guest_id": 2,
    "episode_id": 1
}
```

**Response:**
```json
{
    "message": "Appearance created successfully",
    "appearance": {
        "id": 2,
        "rating": 4,
        "guest_id": 2,
        "episode_id": 1,
        "guest": {
            "id": 2,
            "name": "Ryan Reynolds",
            "occupation": "Actor"
        },
        "episode": {
            "id": 1,
            "date": "2024-01-15",
            "number": 101
        }
    }
}
```

## Testing with Postman

1. Import the `challenge-4-lateshow.postman_collection.json` file into Postman
2. The collection includes:
   - Environment variables for base URL
   - Authentication requests that automatically save JWT tokens
   - All API endpoints with sample data
   - Pre-configured authorization headers for protected routes

### Testing Steps:
1. **Register/Login**: Use the authentication endpoints to get a JWT token
2. **Test Public Routes**: Episodes and Guests endpoints work without authentication
3. **Test Protected Routes**: Use the saved JWT token for Appearances and Episode deletion

## 🗂 Project Structure

```
.
├── server/
│   ├── app.py                 # Flask application factory
│   ├── config.py             # Configuration settings
│   ├── seed.py               # Database seeding script
│   ├── models/
│   │   ├── __init__.py       # Models package
│   │   ├── user.py           # User model
│   │   ├── guest.py          # Guest model
│   │   ├── episode.py        # Episode model
│   │   └── appearance.py     # Appearance model
│   └── controllers/
│       ├── __init__.py       # Controllers package
│       ├── auth_controller.py      # Authentication routes
│       ├── guest_controller.py     # Guest routes
│       ├── episode_controller.py   # Episode routes
│       └── appearance_controller.py # Appearance routes
├── migrations/                     # Database migrations
├── challenge-4-lateshow.postman_collection.json
├── Pipfile                        # Python dependencies
├── .gitignore
└── README.md
```

## Security Features

- **Password Hashing**: Uses Werkzeug's secure password hashing
- **JWT Tokens**: Secure token-based authentication
- **Input Validation**: Validates all user inputs
- **Error Handling**: Proper error responses without exposing sensitive information
- **SQL Injection Protection**: Uses SQLAlchemy ORM for database queries

## Sample Data

The seed script creates:
- 2 users (admin/password123, testuser/test123)
- 8 guests including actors, musicians, and other celebrities
- 6 episodes from January-February 2024
- 8 appearances with ratings

## Deployment Considerations

For production deployment:
1. Update `JWT_SECRET_KEY` and `SECRET_KEY` in config
2. Set `DEBUG = False`
3. Use environment variables for sensitive configuration
4. Configure proper PostgreSQL connection string
5. Set up proper logging
6. Use a production WSGI server like Gunicorn

##  Requirements Checklist

- MVC architecture with proper folder structure
- PostgreSQL database (no SQLite)
- All models with proper relationships and validations
- JWT authentication with Flask-JWT-Extended
- Protected routes requiring authentication
- Cascade delete for episodes → appearances
- Rating validation (1-5)
- Complete seed data
-  All required API routes implemented
- Postman collection with working examples
- Comprehensive README with setup instructions
- Clean error handling and responses

##  GitHub Repository

[https://github.com/caninemanace/late-show-api-challenge](https://github.com/caninemance/late-show-api-challenge)

##  License

MIT License - see LICENSE file for details
