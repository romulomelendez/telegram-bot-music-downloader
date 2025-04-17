FROM python:3.11-slim

WORKDIR /App

COPY . /app

RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
