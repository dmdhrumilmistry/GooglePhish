# DESCRIPTION:	  Deploys GooglePhish in Container
# AUTHOR:		  Dhrumil Mistry <contact@dmdhrumilmistry.me>
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

# install requirements
RUN python -m pip install -r requirements.txt

# check for errors in application
RUN python manage.py check

# migrate database
RUN python manage.py makemigrations
RUN python manage.py migrate

# collect static images
RUN python manage.py collectstatic

# get build arguments (credentials)
ARG dj_email
ARG dj_username
ARG dj_password

# create superuser
ENV DJANGO_SUPERUSER_EMAIL=${dj_email}
ENV DJANGO_SUPERUSER_USERNAME=${dj_username}
ENV DJANGO_SUPERUSER_PASSWORD=${dj_password}
RUN python manage.py createsuperuser --noinput

# expose ports
EXPOSE 8000

# start application
CMD [ "gunicorn", "GooglePhish.wsgi", "-b", "0.0.0.0:8000" ]
