FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY auth /app/auth
COPY entities /app/entities
COPY resolvers /app/resolvers
COPY services /app/services
COPY config.py /app/config.py
COPY main.py /app/main.py

RUN python3 -m pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
