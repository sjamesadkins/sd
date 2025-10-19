FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src
COPY pyproject.toml ./
RUN pip install --upgrade pip && pip install fastapi uvicorn
COPY src ./src
EXPOSE 8000

