survey_chatbot/
├── pyproject.toml          # Project metadata and dependencies
├── README.md               # Project documentation
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore file
├── docker-compose.yml      # Docker compose configuration
├── Dockerfile              # Docker configuration
│
├── app/                    # Main application package
│   ├── __init__.py
│   ├── main.py             # FastAPI app initialization and router inclusion
│   ├── config.py           # Configuration settings
│   ├── constants.py        # Application constants
│   │
│   ├── api/                # API endpoints
│   │   ├── __init__.py
│   │   ├── router.py       # Main API router
│   │   ├── v1/             # API version 1
│   │   │   ├── __init__.py
│   │   │   ├── router.py   # v1 router
│   │   │   ├── surveys.py  # Survey endpoints
│   │   │   ├── responses.py # Response endpoints
│   │   │   ├── chatbot.py  # Chatbot conversation endpoints
│   │   │   ├── auth.py     # Authentication endpoints
│   │   │   └── users.py    # User endpoints
│   │
│   ├── core/               # Core application modules
│   │   ├── __init__.py
│   │   ├── security.py     # Authentication & authorization
│   │   ├── exceptions.py   # Custom exceptions
│   │   └── logging.py      # Logging configuration
│   │
│   ├── services/           # Business logic services
│   │   ├── __init__.py
│   │   ├── survey_service.py    # Survey management logic
│   │   ├── response_service.py  # Survey response handling
│   │   ├── chatbot_service.py   # Chatbot orchestration
│   │   ├── nlp_service.py       # Natural language processing
│   │   └── user_service.py      # User management
│   │
│   ├── models/             # Data models
│   │   ├── __init__.py
│   │   ├── survey.py       # Survey models
│   │   ├── response.py     # Response models
│   │   ├── chatbot.py      # Chatbot conversation models
│   │   └── user.py         # User models
│   │
│   ├── schemas/            # Pydantic schemas for request/response validation
│   │   ├── __init__.py
│   │   ├── survey.py       # Survey schemas
│   │   ├── response.py     # Response schemas
│   │   ├── chatbot.py      # Chatbot conversation schemas
│   │   └── user.py         # User schemas
│   │
│   ├── db/                 # Database modules
│   │   ├── __init__.py
│   │   ├── session.py      # Database session management
│   │   ├── models.py       # SQLAlchemy ORM models
│   │   └── repositories/   # Repository pattern implementations
│   │       ├── __init__.py
│   │       ├── base.py     # Base repository
│   │       ├── survey_repository.py
│   │       ├── response_repository.py
│   │       ├── chatbot_repository.py
│   │       └── user_repository.py
│   │
│   ├── utils/              # Utility functions
│   │   ├── __init__.py
│   │   ├── helpers.py      # General helpers
│   │   └── validators.py   # Custom validators
│
├── tests/                  # Test suite
│   ├── __init__.py
│   ├── conftest.py         # Test fixtures
│   ├── api/                # API tests
│   │   ├── __init__.py
│   │   ├── test_surveys.py
│   │   ├── test_responses.py
│   │   ├── test_chatbot.py
│   │   └── test_users.py
│   │
│   ├── services/           # Service tests
│   │   ├── __init__.py
│   │   ├── test_survey_service.py
│   │   ├── test_response_service.py
│   │   ├── test_chatbot_service.py
│   │   └── test_user_service.py
│   │
│   └── repositories/       # Repository tests
│       ├── __init__.py
│       ├── test_survey_repository.py
│       ├── test_response_repository.py
│       ├── test_chatbot_repository.py
│       └── test_user_repository.py
│
├── alembic/                # Database migrations
│   ├── versions/
│   ├── env.py
│   └── alembic.ini
│
└── scripts/                # Utility scripts
    ├── seed_db.py          # Database seeding
    └── generate_openapi.py # OpenAPI spec generation