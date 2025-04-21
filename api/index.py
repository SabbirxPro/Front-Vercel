import os
import json
from http import HTTPStatus
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get('TOKEN')

# Font transformation functions
def transform_text(text, style):
    fonts = {
        'bold': {'a': '𝗮', 'b': '𝗯', 'c': '𝗰', ...},  # Add all characters
        'italic': {'a': '𝘢', 'b': '𝘣', 'c': '𝘤', ...},
        # Add other styles from original bot
    }
    return ''.join(fonts[style].get(c, c) for c in text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✨ Send me text to style it in different fonts!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    styled = "\n".join([
        f"𝐁𝐨𝐥𝐝: {transform_text(text, 'bold')}",
        f"𝘐𝘵𝘢𝘭𝘪𝘤: {transform_text(text, 'italic')}",
        # Add other styles
    ])
    await update.message.reply_text(styled)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

async def handler(request):
    if request.method == 'POST':
        data = await request.json()
        update = Update.de_json(data, app.bot)
        await app.initialize()
        await app.process_update(update)
        return {'statusCode': HTTPStatus.OK, 'body': 'OK'}
    return {'statusCode': HTTPStatus.METHOD_NOT_ALLOWED}
