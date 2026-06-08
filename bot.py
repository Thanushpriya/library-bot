from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

print("working")

TOKEN = "8660373411:AAHyea3qQqMn7i1V_TrzPaTPc4zV_z_CH1I"

books = {
    "harry potter": {
        "status": "Available ✅",
        "content": "Harry Potter is a fantasy novel about a young wizard."
    },
    "python programming": {
        "status": "Available ✅",
        "content": "Python Programming is used for AI, web development and automation."
    },
    "data science": {
        "status": "Not Available ❌",
        "content": "Data Science involves statistics, ML and data analysis."
    },
    "java": {
        "status": "Available ✅",
        "content": "Java is a high-level programming language."
    }
}

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower().strip()
    msg = " ".join(msg.split())

    # ---------------- GREETING ----------------
    if msg in ["hello", "hi", "hey"]:
        await update.message.reply_text(
            "👋 Welcome to Library Bot!\n\nType /help to see commands 📚"
        )
        return

    # ---------------- START ----------------
    if msg == "/start":
        await update.message.reply_text(
            "📚 Welcome to Library Bot\n\n"
            "📌 Available Commands:\n"
            "👉 /books - list all books\n"
            "👉 /help - show help menu\n"
            "👉 /about - about this bot\n\n"
            "📖 Book Commands:\n"
            "👉 open <book name>\n"
            "👉 issue <book name>\n"
            "👉 return <book name>\n\n"
            "Type 'hello' for greeting 👋"
        )
        return

    # ---------------- HELP ----------------
    if msg == "/help":
        await update.message.reply_text(
            "📌 HELP MENU\n\n"
            "👉 /start - Start bot\n"
            "👉 /books - List all books\n"
            "👉 /about - About bot\n\n"
            "📖 Book Commands:\n"
            "👉 open <book name>\n"
            "👉 issue <book name>\n"
            "👉 return <book name>\n\n"
           
        )
        return

    # ---------------- ABOUT ----------------
    if msg == "/about":
        await update.message.reply_text(
            "🤖 Library Bot\n\n"
            "Built using Python + Telegram Bot API\n\n"
            "Features:\n"
            "✔ View books\n"
            "✔ Read book content\n"
            "✔ Issue & Return system (demo)"
        )
        return

    # ---------------- BOOK LIST ----------------
    if msg == "/books":
        book_list = "\n".join([f"📖 {b.title()}" for b in books])
        await update.message.reply_text(book_list)
        return

    # ---------------- OPEN BOOK ----------------
    if msg.startswith("open "):
        book_name = msg.replace("open ", "").replace("book", "").strip()

        for book in books:
            if book_name in book:
                await update.message.reply_text(
                    f"📖 {book.title()}\n\n{books[book]['content']}"
                )
                return

        await update.message.reply_text("Book not found ❌")
        return

    # ---------------- ISSUE BOOK ----------------
    if msg.startswith("issue "):
        book_name = msg.replace("issue ", "").replace("book", "").strip()

        if book_name in books:
            await update.message.reply_text(
                f"📕 {book_name.title()} issued successfully ✅"
            )
        else:
            await update.message.reply_text("Book Not Found ❌")
        return

    # ---------------- RETURN BOOK ----------------
    if msg.startswith("return "):
        book_name = msg.replace("return ", "").replace("book", "").strip()

        if book_name in books:
            await update.message.reply_text(
                f"📗 {book_name.title()} returned successfully ✅"
            )
        else:
            await update.message.reply_text("Book Not Found ❌")
        return

    # ---------------- STATUS CHECK ----------------
    if msg in books:
        await update.message.reply_text(
            f"📚 {msg.title()}\nStatus: {books[msg]['status']}"
        )
    else:
        await update.message.reply_text("Book Not Found ❌")


# ---------------- RUN BOT ----------------
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot Started...")
app.run_polling()