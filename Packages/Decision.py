import json
from Packages.Commands import *
from Packages.Database import check_user
from Packages.Downloader import download_file

def check_valid_commands(Command):
    if Command in {"/start","/help"}:
        return True
    else:
        return False

def decision_making(update):
    if update.get("message") != None:
        #print(json.dumps(getUpdates, indent=4))
        update = update["message"]
        if "from" in update:
            update1 = update["from"]
            from_id = update1["id"]
            from_is_bot = update1["is_bot"]
            from_first_name = update1["first_name"] if "first_name" in update1 else ""
            from_last_name = update1["last_name"] if "last_name" in update1 else ""
            from_username = update1["username"] if "username" in update1 else ""
            from_language_code = update1["language_code"] if "language_code" in update1 else ""
            if from_is_bot == True:
                from_can_join_groups = update1[
                "can_join_groups"] if "can_join_groups" in update1 else ""
                from_can_read_all_group_messages = update1[
                "can_read_all_group_messages"
                ] if "can_read_all_group_messages" in update1 else ""
                from_supports_inline_queries = update1[
                "supports_inline_queries"
                ] if "supports_inline_queries" in update1 else ""

        if "chat" in update:
            update1 = update["chat"]
            chat_id = update1["id"]
            chat_type = update1["first_name"]
            chat_title = update1["first_name"] if "first_name" in update1 else ""
            chat_username = update1["username"] if "username" in update1 else ""
            chat_first_name = update1["first_name"] if "first_name" in update1 else ""
            chat_last_name = update1["last_name"] if "last_name" in update1 else ""

        text = update["text"] if "text" in update else ''

        if text == '/start':
            is_new_user = check_user(chat_id, from_first_name, from_last_name, from_username)
            if is_new_user:
                start_new_user(chat_id)
            else:
                start(chat_id)
        else:
            filename = download_file(text)
            if filename == None:
                text = f'Failed to download file: ❌\n{text}'
                send_message(chat_id, text)
            else:
                new_link = f"https://mehrshadina.ir/media/uploader_bot/{filename}"
                send_new_link(chat_id, filename, new_link)