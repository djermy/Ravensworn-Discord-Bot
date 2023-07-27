FROM python:3.9-alpine

WORKDIR /app

COPY venv venv 
RUN source venv/bin/activate

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "./main.py"]