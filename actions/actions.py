
def start(update, context):
    if context.args[0] == 'return':
        context.bot.send_message(chat_id=update.effective_chat.id, text="return")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="main")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)