FROM python:3.11-slim

WORKDIR /App

COPY . .

RUN apt-get update && apt-get install -y ffmpeg
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
