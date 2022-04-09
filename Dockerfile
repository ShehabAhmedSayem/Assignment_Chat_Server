# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY django-insecure-$zwrywai49gc(*6g^es66_*p3@rjm(#9!1@s3lw*civlz9wakt
ENV DEBUG 1
ENV MESSAGE_SERVER_IP 171.22.0.5:8000
ENV AUTO_REPLY 1
ENV MESSAGE_SENDING_GAP_IN_SECONDS 20


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app
RUN python manage.py migrate
ENTRYPOINT [ "python", "manage.py", "runserver" ]
CMD [ "0.0.0.0:8000" ]
