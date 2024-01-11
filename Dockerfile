FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

WORKDIR /app

RUN pip3 install "poetry==1.7.1" 'dulwich==0.21.5'

COPY . /app

# RUN pip install -r requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

RUN pip3 install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]