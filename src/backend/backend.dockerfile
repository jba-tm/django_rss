# Dockerfile
# pull official base image
FROM python:3.9.6
# accept arguments
ARG PIP_REQUIREMENTS=production.txt
ARG DATABASE_USER


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /home/${DATABASE_USER}
# set work directory
WORKDIR /home/${DATABASE_USER}

# create and activate virtual environment
RUN python3 -m venv venv

RUN ./venv/bin/python3 -m pip install pip setuptools wheel --upgrade

# copy and install pip requirements
#COPY --chown=${DATABASE_USER} ./requirements/ /home/${DATABASE_USER}/requirements/
COPY  ./requirements /home/${DATABASE_USER}/requirements/

RUN ./venv/bin/pip3 install -r /home/${DATABASE_USER}/requirements/${PIP_REQUIREMENTS}

# copy Django project files
#COPY --chown=${DATABASE_USER} ./ /home/${DATABASE_USER}/
COPY ./ /home/${DATABASE_USER}/
