FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6 libc6 libstdc++6 && \
    rm -rf /var/lib/apt/lists/*

RUN which ffmpeg

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENV PATH="/usr/bin:${PATH}"

CMD ["python", "bot.py"]
