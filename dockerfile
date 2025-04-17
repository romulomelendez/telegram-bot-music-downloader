FROM python:3.11

RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
