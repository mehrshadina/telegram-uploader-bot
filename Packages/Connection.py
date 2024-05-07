import requests

TOKEN = "7041348703:AAFe0MpJfHNph0ZwBho7MP3wXUXuN33szf4"
URL = "https://api.telegram.org/bot%s/"%TOKEN

proxies = {
   'http': 'socks5://127.0.0.1:9050',
   'https': 'socks5://127.0.0.1:9050'
}

def send_url(url):
    print(url)
    response = requests.get(url) # you can use this option: proxies=proxies
    return response.json()

def json_from_url(url):
    getUpdates = send_url(url)
    return getUpdates

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = json_from_url(url)
    return js

def send_message(chat_id, text, reply_markup=dict(), markdown=False, reply_to=None):
    if markdown:
        json = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'MarkdownV2',
            'reply_markup': reply_markup,
            'reply_to_message_id': reply_to
        }
    else:
        json = {
            'chat_id': chat_id,
            'text': text,
            'reply_markup': reply_markup,
            'reply_to_message_id': reply_to
        }

    response = requests.post(URL + "sendMessage", json=json) # you can use this option: proxies=proxies
    print(response.json())

def send_sticker(chat_id, sticker_file_id):
    data = {
        'chat_id': chat_id,
        'sticker': sticker_file_id,
    }
    re = requests.post(URL + "sendSticker", data=data) # you can use this option: proxies=proxies
    print(re.json())

def send_document(doc, chat_id):
    files = {'document': open("/address")}
    requests.post(URL + "sendDocument?chat_id={}".format(chat_id), files=files)

def send_image(chat_id):
    files = {'photo': open("/address")}
    requests.post(URL + "sendPhoto?chat_id={}".format(chat_id), files=files)
