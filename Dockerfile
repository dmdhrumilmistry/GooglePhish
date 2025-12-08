# DESCRIPTION:	  Deploys GooglePhish in Container
# AUTHOR:		  Dhrumil Mistry <contact@dmdhrumilmistry.tech>
# COMMENTS:
#	This file describes how to deploy GooglePhish
#	in a container with all dependencies installed.
# USAGE:
#	# Download googlephish Dockerfile
#	wget [link]
#
#	# Build image
#	docker build -t googlephish .
#
#   # run docker container
#	docker run -d -p 80:8000 googlephish
#

# Use python slim as base image
FROM python:3.12-slim

# Set environment variables
ENV POETRY_HOME="/opt/poetry"
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV GP_DIR="/GooglePhish"

# Set working directory
WORKDIR $GP_DIR

# Install system dependencies for Poetry and other build tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Copy project files
COPY . .

# Install project dependencies with Poetry without creating virtualenv (use system python)
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

# Check for errors in application
RUN poetry run python manage.py check

# Make migrations and migrate database
RUN poetry run python manage.py makemigrations
RUN poetry run python manage.py migrate

# Collect static files
RUN poetry run python manage.py collectstatic --noinput

# Set environment variables for superuser creation
ENV DJANGO_SUPERUSER_EMAIL=admin@mail.local
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=G00g13P#15#23

# Create superuser without input prompts
RUN poetry run python manage.py createsuperuser --noinput || echo "Superuser already exists."

# Expose port
EXPOSE 8000

# Start the application using gunicorn
CMD ["poetry", "run", "gunicorn", "GooglePhish.wsgi:application", "-b", "0.0.0.0:8000"]
