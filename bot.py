import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🔧 Santexnika", "⚡ Elektr"],
        ["📦 Buyurtma berish", "📞 Aloqa"],
    ]

    await update.message.reply_text(
        "Assalomu alaykum! 👋\n\n"
        "Suyan — muammoingizni ayting, yechimini topamiz.\n\n"
        "Kerakli xizmatni tanlang:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True
        ),
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🔧 Santexnika":
        await update.message.reply_text(
            "🔧 Santexnika xizmatlari:\n\n"
            "• Kranni ta'mirlash\n"
            "• Suv quvurlari\n"
            "• Rakovina va unitaz\n"
            "• Oqishlarni bartaraf etish\n\n"
            "Buyurtma berish uchun «📦 Buyurtma berish»ni bosing."
        )

    elif text == "⚡ Elektr":
        await update.message.reply_text(
            "⚡ Elektr xizmatlari:\n\n"
            "• Rozetka va kalit\n"
            "• Chiroq o‘rnatish\n"
            "• Elektr simlari\n"
            "• Nosozliklarni aniqlash\n\n"
            "Buyurtma berish uchun «📦 Buyurtma berish»ni bosing."
        )

    elif text == "📦 Buyurtma berish":
        context.user_data["ordering"] = True

        await update.message.reply_text(
            "📦 Buyurtma qabul qilish\n\n"
            "Muammoingizni batafsil yozing.\n"
            "Masalan: «Oshxonadagi krandan suv oqyapti»."
        )

    elif text == "📞 Aloqa":
        await update.message.reply_text(
            "📞 Suyan bilan bog‘lanish:\n\n"
            "+998 77 713 28 05\n"
            "+998 93 832 55 50\n"
            "+998 70 052 81 67"
        )

    elif context.user_data.get("ordering"):
        context.user_data["ordering"] = False

        await update.message.reply_text(
            "✅ Buyurtmangiz qabul qilindi!\n\n"
            "Mutaxassisimiz siz bilan bog‘lanadi.\n"
            "Suyan — muammoingizni ayting, yechimini topamiz."
        )

    else:
        await update.message.reply_text(
            "Iltimos, menyudagi xizmatlardan birini tanlang yoki /start buyrug‘ini yuboring."
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    )

    print("Suyan bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
