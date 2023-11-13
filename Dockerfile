#  FROM mysql:8.0.32
#  ENV MYSQL_ROOT_PASSWORD password
#  COPY ./database/01_create_database.sql /docker-entrypoint-initdb.d/data.sql01

FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt update \
  && apt install -y python3-dev netcat-openbsd default-libmysqlclient-dev build-essential pkg-config \
  && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["gunicorn", "super_portfolio.wsgi", "--bind", "0.0.0.0:8000"]