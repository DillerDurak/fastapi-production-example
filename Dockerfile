FROM python:3.11.2-alpine

EXPOSE 8000

WORKDIR /code

COPY . /code

RUN pip install --upgrade pip & pip install -r requirements.txt


CMD ["uvicorn", "production_fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]
