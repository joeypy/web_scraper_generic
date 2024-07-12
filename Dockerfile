FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

RUN mkdir -p /app/data

CMD ["python", "main.py"]