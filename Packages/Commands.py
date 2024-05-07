from Packages.Connection import send_message

def start_new_user(chat_id):
    text = (
        "Hello my friend ✋\n"
        "This bot is made to download any file without government filters and sanctions.\n"
        "\n"
        "🌐 How to use?\n"
        "💠 its easy to use, just send the download link and i will give you a new link without restrictions.\n"
        "\n"
        "=================================\n"
        "⛔️Attention: Dont send links larger than 10 GB.\n"
    )
    send_message(chat_id, text)

def start(chat_id):
    text = (
        "🌐 How to use?\n"
        "💠 its easy to use, just send the download link and i will give you a new link without restrictions.\n"
        "\n"
        "=================================\n"
        "⛔️Attention: Dont send links larger than 10 GB.\n"
    )
    send_message(chat_id, text)

def send_new_link(chat_id, filename, link):
    text = (
        f"File downloaded successfully: `{filename}` ✅\n"
        "Here is new link:\n"
        f"*[Download]({link})*"
    )
    print(text)
    send_message(chat_id, text, markdown=True)

def help(chat_id):
    text = "You have send /help command"
    send_message(chat_id, text)

def unknow(chat_id):
    text = "I don't undresstand what you said!\nuse the keys"
    #keyboard = """&reply_markup={"keyboard": [["key1","key2"],["key3","key4","key5"]], "resize_keyboard":true}"""
    send_message(chat_id, text) # you must send keyboard for send_message function
