from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import subprocess
from dotenv import load_dotenv
import os
import glob

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')


# /start command
async def start(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm MOJO 🎵! Send me a Youtube Video Link or a artista/song name")


# Function to download audio
def download_audio(consult_url, output_file):

    if "youtube.com" in consult_url or "youtu.be" in consult_url:
        url = consult_url
    else:
        url = f"ytsearch1:{consult_url}"

    command = [
        'yt-dlp',
        '--cookies', 'cookies.txt',
        '-x', '--audio-format', 'mp3',
        '-o', '%(title)s.mojo.%(ext)s',
        url
    ]
    subprocess.run(command)


async def receive_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"🎵 Downloading audio of this video: {text}")

    file_name = '%(title)s.mojo.%(ext)s'
    download_audio(text, file_name)

    audio_files = glob.glob("*.mojo.mp3")
    if audio_files:
        audio_path = audio_files[0]
        await update.message.reply_audio(audio=open(audio_path, 'rb'))
        os.remove(audio_path)
    else:
        await update.message.reply_text("❌ Fail to download music!")



def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_message))
    app.run_polling()

if __name__ == '__main__':
    main()