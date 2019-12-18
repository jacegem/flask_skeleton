FROM python:3.6

ENV PIP_DISABLE_PIP_VERSION_CHECK=on
RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-interaction

COPY . .

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]