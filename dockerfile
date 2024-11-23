FROM python:3.12
WORKDIR /app
RUN pip install poetry
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root
COPY . .
CMD ["poetry", "run", "python", "cli.py", "api"]