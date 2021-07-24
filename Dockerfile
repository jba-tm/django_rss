# Dockerfile
# pull official base image
FROM python:3.8.8
# accept arguments
ARG PIP_REQUIREMENTS=production.txt
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN echo ${DJANGO_SECRET_KEY}


# install dependencies
RUN pip install --upgrade pip setuptools wheel
# create user for the Django project
RUN useradd -ms /bin/bash project_user
# set current user
USER project_user
# set work directory
WORKDIR /home/backend
# create and activate virtual environment
RUN python3 -m venv venv

RUN ./venv/bin/python3 -m pip install pip setuptools wheel --upgrade

# copy and install pip requirements
COPY --chown=project_user ./src/backend/requirements/ /home/backend/requirements/
RUN ./venv/bin/pip3 install -r /home/backend/requirements/${PIP_REQUIREMENTS}
# copy Django project files
COPY --chown=project_user ./src/backend/ /home/backend/
