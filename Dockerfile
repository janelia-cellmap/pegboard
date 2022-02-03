FROM python:3.9.6-slim

RUN apt-get update && apt install -y netcat default-libmysqlclient-dev gcc

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# entrypoint setup
WORKDIR /startup
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /startup/entrypoint.sh
RUN chmod +x /startup/entrypoint.sh

WORKDIR /code

COPY ./requirements.txt ./
RUN pip install -r requirements.txt


COPY ./app .

EXPOSE 8000
ENTRYPOINT ["/startup/entrypoint.sh"]
