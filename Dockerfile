FROM python:3.11-slim as python-base

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

ENV DATABASE_URL "NULL"
ENV DJANGO_SETTINGS_MODULE "core.settings.base"
ENV PORT 8000
ENV WORKERS 4
ENV PATH "/root/.local/bin:$PATH"
# Add your private package credentials here if needed
# ENV POETRY_HTTP_BASIC_PRIVATE_PASSWORD="your-token"
# ENV POETRY_HTTP_BASIC_PRIVATE_USER="your-user"

WORKDIR /app
EXPOSE 8000

RUN apt-get update && apt-get install -yq libpq-dev gcc curl openssh-client
RUN curl -sSL https://install.python-poetry.org | python3 -
# Download public key for gitlab.com
RUN mkdir -p -m 0700 ~/.ssh && ssh-keyscan gitlab.com >> ~/.ssh/known_hosts

FROM python-base as linters
COPY poetry.lock pyproject.toml ./
RUN --mount=type=ssh poetry config virtualenvs.create false \
    && poetry install
COPY . /app/

FROM python-base as production
COPY pyproject.toml ./
# Copy lock file if it exists, otherwise poetry will generate it
COPY poetry.lock* ./
RUN --mount=type=ssh poetry config virtualenvs.create false \
&& poetry lock \
&& poetry install --no-root --without dev

ADD . /app/
RUN python manage.py collectstatic --noinput

ADD run-fastapi.sh run-django.sh /
RUN chmod +x /run-fastapi.sh /run-django.sh

CMD [ "/run-fastapi.sh"]
