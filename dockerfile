FROM python:3.13-slim

RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/bin:${PATH}"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
