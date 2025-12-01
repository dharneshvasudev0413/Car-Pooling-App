from datetime import timedelta

# DATABASE
# For dev: SQLite (file in the user-service folder)
DATABASE_URL = "sqlite:///./users.db"
# Later for Postgres (example):
# DATABASE_URL = "postgresql://user:password@db-host/db-name" or
# DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"


# JWT / SECURITY
SECRET_KEY = "super-secret-key-change-this"  # change for real deployment
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hour

# RABBITMQ
RABBITMQ_HOST = "localhost"
RABBITMQ_QUEUE = "user.events"
