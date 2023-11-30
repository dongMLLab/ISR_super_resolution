FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

WORKDIR /app

RUN pip install -r requirements.txt

COPY . .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]