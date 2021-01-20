FROM python:3.8.3-alpine

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirement.txt

CMD ["python", "app.py"]
