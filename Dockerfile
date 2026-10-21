
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ templates/
COPY static/ static/

RUN mkdir -p /app/data

ENV TODO_DATABASE=/app/data/tasks.db

EXPOSE 5000

CMD ["python", "app.py"]
