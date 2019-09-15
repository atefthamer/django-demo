# https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99
# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# # The enviroment variable ensures that the python output is set straight
# # to the terminal with out buffering it first
# ENV PYTHONUNBUFFERED 1

# # create root directory for our project in the container
# RUN mkdir /application_demo

# # Set the working directory to /music_service
# WORKDIR /application_demo

# # Copy the current directory contents into the container at /music_service
# ADD . /application_demo/

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

COPY ./requirements.txt /requirements.txt
COPY ./wait-for-it.sh /wait-for-it.sh
RUN pip install -r /requirements.txt

RUN mkdir /application_demo

WORKDIR /application_demo
COPY ./application_demo /application_demo



#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
