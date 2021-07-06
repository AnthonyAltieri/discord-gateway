FROM python:3.9.0

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.6 \
  POETRY_VIRTUALENVS_CREATE=false

WORKDIR /code

RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry install --no-dev --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY . /code


CMD python -m discord_gateway