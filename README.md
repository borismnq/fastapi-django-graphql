# Django GraphQL Federation Template

A production-ready template for building GraphQL Federation services using Django, FastAPI, and Strawberry GraphQL.


## 🚀 Tech Stack

### Core Framework
- **Django 5.0+** - Web framework for database models and admin interface
- **FastAPI 0.110+** - Modern, fast web framework for building APIs
- **Strawberry GraphQL 0.252+** - Python GraphQL library with Federation 2 support
- **Pydantic 2.6.4** - Data validation (pinned for Strawberry compatibility)

### Database
- **PostgreSQL** - Primary database (via psycopg2-binary)
- **SQLite** - Default fallback for development
- **dj-database-url** - Database configuration from environment variables

### GraphQL & API
- **Strawberry GraphQL** - Type-safe GraphQL schema with Python dataclasses
- **GraphQL Federation 2** - Apollo Federation support for microservices
- **graphql-relay** - Relay-style pagination support

### Server & Deployment
- **Gunicorn 22.0+** - WSGI HTTP Server
- **Uvicorn 0.29+** - ASGI server for FastAPI
- **Docker** - Containerization support

### Monitoring & Logging
- **Prometheus FastAPI Instrumentator** - Metrics and monitoring
- **Fluent Logger** - Structured logging support

### Development Tools
- **Poetry** - Dependency management
- **Black** - Code formatter
- **isort** - Import sorting
- **Pylint** - Code linting
- **pytest** - Testing framework
- **pytest-django** - Django testing utilities
- **Syrupy** - Snapshot testing

### Additional Libraries
- **PyJWT** - JWT token handling
- **Requests & HTTPX** - HTTP clients
- **Pydantic Settings** - Settings management
- **python-dotenv** - Environment variable management
- **Boto3** - AWS SDK (optional)
- **Pandas & OpenPyXL** - Data processing (optional)

## 📁 Project Structure

```
.
├── apps/
│   └── api/                    # Main API application
│       ├── schema/             # GraphQL schema definitions
│       │   ├── queries.py      # GraphQL queries
│       │   ├── mutations.py    # GraphQL mutations
│       │   └── types.py        # GraphQL types
│       ├── models.py           # Django models
│       ├── admin.py            # Django admin configuration
│       ├── apps.py             # App configuration
│       └── urls.py             # URL routing
├── core/                       # Core project settings
│   ├── settings/               # Django settings
│   │   └── base.py            # Base settings
│   ├── utils/                  # Utility functions
│   │   ├── permissions.py     # GraphQL permissions
│   │   ├── schema.py          # GraphQL utilities
│   │   ├── models.py          # Model utilities
│   │   └── settings.py        # Settings utilities
│   ├── asgi.py                # ASGI configuration (FastAPI + Django)
│   ├── wsgi.py                # WSGI configuration
│   ├── urls.py                # Main URL configuration
│   ├── schema.py              # GraphQL schema root
│   └── config.py              # Application configuration
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker Compose (create if needed)
├── pyproject.toml             # Poetry dependencies
├── poetry.lock                # Locked dependencies
├── manage.py                  # Django management script
├── gunicorn.conf.py           # Gunicorn configuration
├── run-fastapi.sh             # FastAPI startup script
├── run-django.sh              # Django startup script
└── .env.example               # Environment variables template
```

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.13+
- Poetry
- PostgreSQL (optional, SQLite works for development)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd django-graphql-federation-template
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Run migrations**
   ```bash
   poetry run python manage.py migrate
   ```

5. **Create a superuser** (optional)
   ```bash
   poetry run python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   # Using FastAPI (recommended for GraphQL)
   poetry run uvicorn core.asgi:fastapp --reload --port 8000
   
   # Or using Django
   poetry run python manage.py runserver
   ```

## 🚀 Running the Application

### Development Mode

**FastAPI with hot reload:**
```bash
poetry run uvicorn core.asgi:fastapp --reload --port 8000
```

**Django development server:**
```bash
poetry run python manage.py runserver
```

### Production Mode

**Using Gunicorn (FastAPI):**
```bash
./run-fastapi.sh
```

**Using Gunicorn (Django):**
```bash
./run-django.sh
```

### Docker

```bash
docker build -t django-graphql-federation .
docker run -p 8000:8000 django-graphql-federation
```

## 🛠️ Make Commands

```bash
make setup            # Install dependencies and run migrations
make run              # Run development server
make test             # Run tests
make format           # Format code (black + isort)
make docker-up        # Start Docker containers
make docker-down      # Stop Docker containers
```

Run `make help` to see all available commands.

## 📊 GraphQL Endpoints

- **GraphQL Playground**: `http://localhost:8000/api/graphql/`
- **GraphQL Schema**: `http://localhost:8000/api/graphql/graphql`
- **Health Check**: `http://localhost:8000/api/health/`
- **Application Info**: `http://localhost:8000/api/info/`
- **Metrics**: `http://localhost:8000/metrics`

## 🔐 Authentication & Permissions

The template includes example permission classes in `core/utils/permissions.py`:

- `IsAuthenticated` - Checks if user is authenticated
- `IsAdmin` - Checks if user has admin privileges

Customize these based on your authentication strategy.

## 🧪 Testing

```bash
# Run all tests
poetry run pytest

# Run with coverage
poetry run pytest --cov=apps --cov=core

# Run specific test file
poetry run pytest apps/api/tests/test_schema.py
```

## 🎨 Code Quality

```bash
# Format code
poetry run black .

# Sort imports
poetry run isort .

# Lint code
poetry run pylint apps/ core/

# Run all checks
poetry run black . && poetry run isort . && poetry run pylint apps/ core/
```

## 📝 GraphQL Schema Example

The template includes working examples using Django ORM with the `ExampleModel`:

### Queries
```graphql
# Simple greeting
query {
  hello(name: "World")
}

# Get all examples from database
query {
  examples {
    id
    name
    description
    isActive
    createdAt
    updatedAt
  }
}

# Filter active examples
query {
  examples(isActive: true) {
    id
    name
  }
}

# Get single example by ID
query {
  example(id: "1") {
    id
    name
    description
  }
}

# Search examples by name
query {
  searchExamples(name: "test") {
    id
    name
  }
}
```

### Mutations
```graphql
# Create new example
mutation {
  createExample(input: {
    name: "New Example"
    description: "This is a new example"
    isActive: true
  }) {
    id
    name
    createdAt
  }
}

# Update existing example
mutation {
  updateExample(id: "1", input: {
    name: "Updated Example"
    description: "Updated description"
    isActive: false
  }) {
    id
    name
    updatedAt
  }
}

# Delete example
mutation {
  deleteExample(id: "1")
}
```

## 🔧 Configuration

### Environment Variables

See `.env.example` for all available configuration options.

Key variables:
- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (True/False)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `GRAPHQL_CONNECTION_MAX_RESULTS` - Max results for GraphQL connections

### Django Admin

Access the Django admin at `http://localhost:8000/admin/` after creating a superuser.

## 🌐 Apollo Federation

This template is configured for Apollo Federation 2. To use it as a subgraph:

1. Update `core/schema.py` with your federated entities
2. Add `@strawberry.federation.type(keys=["id"])` to your types
3. Implement reference resolvers
4. Configure your Apollo Gateway to include this subgraph

## 📚 Additional Resources

### Project Documentation
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines

### External Documentation
- [Strawberry GraphQL Documentation](https://strawberry.rocks/)
- [Django Documentation](https://docs.djangoproject.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Apollo Federation](https://www.apollographql.com/docs/federation/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## 📄 License

This template is open source and available under the MIT License.

## 🙏 Acknowledgments

Built with modern Python tools and best practices for GraphQL Federation services.

