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

## TODO: enhance dockerfile

# choose baseimage
FROM python

# set initial Working Directory
WORKDIR /

# create project directory and set as workding directory
ENV GP_DIR="/GooglePhish"
RUN [ -d ${GP_DIR} ] || mkdir -p ${GP_DIR}
WORKDIR ${GP_DIR}

# copy project files
COPY . .

# install poetry
ENV POETRY_HOME="/poetry"
RUN curl -sSL https://install.python-poetry.org | python3 -

# install requirements
RUN /poetry/bin/poetry install

# check for errors in application
RUN /poetry/bin/poetry run python manage.py check

# migrate database
RUN /poetry/bin/poetry run python manage.py makemigrations
RUN /poetry/bin/poetry run python manage.py migrate

# collect static images
RUN ${POETRY_HOME}/bin/poetry run python manage.py collectstatic

# create superuser
ENV DJANGO_SUPERUSER_EMAIL=admin@mail.local
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=G00g13P#15#23
RUN /poetry/bin/poetry run python manage.py createsuperuser --noinput

# expose ports
EXPOSE 8000

# start application
CMD [ "/poetry/bin/poetry", "run", "gunicorn", "GooglePhish.wsgi", "-b", "0.0.0.0:8000" ]
