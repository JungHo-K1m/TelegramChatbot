import os


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
GAME_URL = "https://lucky-777-jungho-k1ms-projects.vercel.app/"  # Vercel 배포 링크

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎮 행운의 7.77초 잡기", url=GAME_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "행운의 7.77초 게임에 도전하세요!",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🤖 봇이 실행 중입니다. 텔레그램에서 /start를 입력해보세요!")
    app.run_polling()
