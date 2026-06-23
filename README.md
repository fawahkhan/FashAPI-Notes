# FastAPI Product Management System

A simple yet powerful FastAPI application demonstrating CRUD operations (GET, POST, PUT, DELETE) for product management and inventory tracking with a PostgreSQL database connection. Go to /docs to access swagger to test the api's.

## Features

- **RESTful API** - Complete CRUD operations for product management
- **Database Integration** - PostgreSQL database with SQLAlchemy ORM
- **Data Validation** - Pydantic models for request/response validation
- **Dependency Injection** - FastAPI's dependency injection for database sessions
- **Inventory Tracking** - Track product quantities in real-time
- **Initial Data Seeding** - Pre-populate database with sample products

## Project Structure

```
├── main.py                 # FastAPI application and route definitions
├── models.py              # Pydantic models for request/response validation
├── database_models.py     # SQLAlchemy ORM models
├── database.py            # Database configuration and session management
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (database URL)
└── .gitignore            # Git ignore file
```

## Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd FastAPI
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Setup & Configuration

1. **Create a PostgreSQL database**
   - Install PostgreSQL if not already installed
   - Create a new database for the project

2. **Configure environment variables**
   - Create a `.env` file in the project root
   - Add your database URL:
     ```
     db_url=postgresql://username:password@localhost/database_name
     ```

3. **Initialize the database**
   - Database tables are automatically created when the application starts
   - Sample products are seeded into the database on first run

## Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

### Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Health Check
- **GET** `/` - Returns greeting message

### Product Operations

| Method | Endpoint | Description |
|--------|----------|-------------|
| **GET** | `/products` | Retrieve all products |
| **GET** | `/product/{id}` | Retrieve a product by ID |
| **POST** | `/product` | Create a new product |
| **PUT** | `/product/{id}` | Update an existing product |
| **DELETE** | `/product/{id}` | Delete a product |

### Request/Response Examples

**Get All Products**
```bash
curl http://localhost:8000/products
```

**Get Product by ID**
```bash
curl http://localhost:8000/product/1
```

**Create Product**
```bash
curl -X POST http://localhost:8000/product \
  -H "Content-Type: application/json" \
  -d '{
    "id": 5,
    "name": "Keyboard",
    "description": "Mechanical keyboard",
    "price": 149.99,
    "quantity": 15
  }'
```

**Update Product**
```bash
curl -X PUT http://localhost:8000/product/1 \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "name": "Smartphone",
    "description": "Latest model phone",
    "price": 799.99,
    "quantity": 5
  }'
```

**Delete Product**
```bash
curl -X DELETE http://localhost:8000/product/1
```

## Database Schema

### Product Table

| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key |
| name | String | - |
| description | String | - |
| price | Float | - |
| quantity | Integer | - |

## Sample Data

The application includes initial sample products:

1. Phone - Budget phone ($99, qty: 10)
2. Laptop - High-performance laptop ($999, qty: 20)
3. Pen - Budget pen ($9, qty: 100)
4. Table - Best table ($100, qty: 20)

## Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and Object Relational Mapper
- **PostgreSQL** - Relational database
- **Pydantic** - Data validation and serialization
- **Uvicorn** - ASGI web server
- **psycopg2** - PostgreSQL adapter for Python
- **python-dotenv** - Load environment variables from .env file

## Key Concepts Demonstrated

- **Dependency Injection** - Database session management using FastAPI's `Depends()`
- **ORM Usage** - SQLAlchemy models for database operations
- **Pydantic Validation** - Request data validation and serialization
- **Database Sessions** - Proper session lifecycle management
- **CRUD Operations** - Complete Create, Read, Update, Delete functionality

## Notes

- Database tables are automatically created on application startup
- Initial data is only seeded if the database is empty
- All database operations use proper session management to prevent connection leaks
- Pydantic models ensure type safety and validation for all API requests

## Future Enhancements

- Add error handling and custom exception responses
- Implement pagination for product listings
- Add filtering and sorting capabilities
- Include authentication and authorization
- Add unit and integration tests
- Implement logging
- Add API rate limiting

## License

This project is created for learning purposes.
