

FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt update \
  && apt install -y python3-dev netcat-openbsd default-libmysqlclient-dev build-essential pkg-config \
  && pip install --upgrade pip

COPY ./requirements.txt ./

COPY ./dev-requirements.txt ./

COPY ./pyproject.toml ./

RUN pip install -r dev-requirements.txt

COPY ./ ./

CMD ["sh", "entrypoint.sh"]