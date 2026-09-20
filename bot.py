import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

SIGNS = {
    "aries": "♈ Овен",
    "taurus": "♉ Телец",
    "gemini": "♊ Близнецы",
    "cancer": "♋ Рак",
    "leo": "♌ Лев",
    "virgo": "♍ Дева",
    "libra": "♎ Весы",
    "scorpio": "♏ Скорпион",
    "sagittarius": "♐ Стрелец",
    "capricorn": "♑ Козерог",
    "aquarius": "♒ Водолей",
    "pisces": "♓ Рыбы",
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("♈ Овен", callback_data="aries"),
            InlineKeyboardButton("♉ Телец", callback_data="taurus"),
            InlineKeyboardButton("♊ Близнецы", callback_data="gemini"),
        ],
        [
            InlineKeyboardButton("♋ Рак", callback_data="cancer"),
            InlineKeyboardButton("♌ Лев", callback_data="leo"),
            InlineKeyboardButton("♍ Дева", callback_data="virgo"),
        ],
        [
            InlineKeyboardButton("♎ Весы", callback_data="libra"),
            InlineKeyboardButton("♏ Скорпион", callback_data="scorpio"),
            InlineKeyboardButton("♐ Стрелец", callback_data="sagittarius"),
        ],
        [
            InlineKeyboardButton("♑ Козерог", callback_data="capricorn"),
            InlineKeyboardButton("♒ Водолей", callback_data="aquarius"),
            InlineKeyboardButton("♓ Рыбы", callback_data="pisces"),
        ],
    ]

    await update.message.reply_text(
        "🌙 Добро пожаловать в «Гороскоп на каждый день»!\n\n"
        "Выбери свой знак зодиака:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def sign_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    sign = SIGNS[query.data]

    await query.edit_message_text(
        f"{sign}\n\n"
        "🔮 Гороскоп на сегодня\n\n"
        "❤️ Любовь — скоро здесь появится твой прогноз.\n\n"
        "💰 Финансы — скоро здесь появится твой прогноз.\n\n"
        "💼 Работа — скоро здесь появится твой прогноз.\n\n"
        "🌿 Самочувствие — скоро здесь появится твой прогноз.\n\n"
        "✨ Совет дня — скоро здесь появится твой совет.\n\n"
        "🌙 Мы готовим для тебя настоящую систему ежедневных "
        "астрологических прогнозов."
    )


def main():
    token = os.environ.get("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN не найден")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(sign_selected))

    print("Бот запущен!")
    app.run_polling()


if __name__ == "__main__":
    main()
