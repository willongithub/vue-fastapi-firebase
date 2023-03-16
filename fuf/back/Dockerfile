FROM python:3.11

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off

ARG version
LABEL version=$version

COPY pyproject.toml poetry.lock /app/

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    python -m pip install --upgrade pip && \
    poetry export -f requirements.txt --output requirements.txt && \
    python -m pip install -r requirements.txt

COPY . .

RUN useradd back
RUN chown -R back /app
USER back

CMD [ "python", "-m", "back" ]
