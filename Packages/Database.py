from os.path import abspath, exists
import sqlite3 as sl

database_location1 = abspath(__file__)
database_location = database_location1[:-11] + "/Database.db"

def check_database():
    #print(os.path.abspath(database_lacation))
    return exists(database_location)

def create_table():
    con = sl.connect(str(database_location))
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE users (
    chat_id INTEGER,
    first_name TEXT,
    last_name TEXT,
    username TEXT
        );
    """)

    cur.execute("""
        CREATE TABLE channels (
    chat_id_c INTEGER,
    title_c TEXT,
    username_c TEXT,
    status TEXT,
    can_be_edited TEXT,
    can_manage_chat TEXT,
    can_change_info TEXT,
    can_post_messages TEXT,
    can_edit_messages TEXT,
    can_delete_messages TEXT,
    can_invite_users TEXT,
    can_restrict_members TEXT,
    can_promote_members TEXT,
    can_manage_voice_chats TEXT,
    is_anonymous TEXT
        );
    """)
    con.commit()
    con.close()

def check_user(chat_id,first_name="",last_name="",username=""):
    if read_database(1, chat_id) == False: #new_user
        write_in_database(da=[chat_id,first_name,last_name,username])
        return False
    else: #old_user
        return True

def write_in_database(update=False, da=[]):
    con = sl.connect(str(database_location))
    cur = con.cursor()

    if update == False:
        query = "INSERT INTO users (chat_id, first_name, last_name, username) VALUES ({},\"{}\",\"{}\",\"{}\")".format(da[0], da[1], da[2],da[3])
        #print("\n\n", query, "\n\n")
    else:
        """
        if key == "first_name":
            query = "UPDATE users SET \"first_name\" = \"{}\" WHERE chat_id = {}".format(key2, chat_id)
        elif key == "sex":
            query = "UPDATE users SET sex = \"{}\" WHERE chat_id = {}".format(key2, chat_id)
        #print("\n\n", query, "\n\n")
        """
        pass

    cur.execute(query)
    con.commit()
    con.close()

def read_database(number,id_person,chat_id=None):
    #print("we are connected to database telegram")
    con = sl.connect(str(database_location))
    cur = con.cursor()
    if number == 1:
        query = "SELECT chat_id FROM users"
        type(cur.execute(query))
        for chat_id in cur.execute(query):
            if id_person in chat_id:
                return True #hast
        return False

    elif number == 2:
        first_name=None
        query = "SELECT first_name from users WHERE chat_id = {}".format(id_person)
        for x in cur.execute(query):
            first_name = x[0]
        return first_name

def delete_from_database(number, id_person):
    con = sl.connect(str(database_location))
    cur = con.cursor()

    if number == 1:
        query = "DELETE from channels WHERE \"title_c\" = \"{}\"".format(id_person)
    #print("\n\n", query, "\n\n")
    cur.execute(query)
    con.commit()
    con.close()

def write_channel(json, username):
    chat_id_c = json["my_chat_member"]["chat"]["id"]
    title_c = json["my_chat_member"]["chat"]["title"]
    username_c = username
    print(username_c)
    status = json["my_chat_member"]["new_chat_member"]["status"]
    can_be_edited = json["my_chat_member"]["new_chat_member"]["can_be_edited"]
    can_manage_chat = json["my_chat_member"]["new_chat_member"]["can_manage_chat"]
    can_change_info = json["my_chat_member"]["new_chat_member"]["can_change_info"]
    can_post_messages = json["my_chat_member"]["new_chat_member"]["can_post_messages"]
    can_edit_messages = json["my_chat_member"]["new_chat_member"]["can_edit_messages"]
    can_delete_messages = json["my_chat_member"]["new_chat_member"]["can_delete_messages"]
    can_invite_users = json["my_chat_member"]["new_chat_member"]["can_invite_users"]
    can_restrict_members = json["my_chat_member"]["new_chat_member"]["can_restrict_members"]
    can_promote_members = json["my_chat_member"]["new_chat_member"]["can_promote_members"]
    can_manage_voice_chats = json["my_chat_member"]["new_chat_member"]["can_manage_voice_chats"]
    is_anonymous = json["my_chat_member"]["new_chat_member"]["is_anonymous"]

    con = sl.connect(str(database_location))
    cur = con.cursor()
    query = """INSERT INTO channels (
            chat_id_c,
            title_c,
            username_c ,
            status ,
            can_be_edited ,
            can_manage_chat ,
            can_change_info ,
            can_post_messages ,
            can_edit_messages ,
            can_delete_messages ,
            can_invite_users ,
            can_restrict_members ,
            can_promote_members ,
            can_manage_voice_chats ,
            is_anonymous
            )
            VALUES
            (\"{}\",\"{}\",\"{}\",
            \"{}\",\"{}\",\"{}\",
            \"{}\",\"{}\",\"{}\",
            \"{}\",\"{}\",\"{}\",
            \"{}\",\"{}\",\"{}\"
            )""".format(chat_id_c,title_c,username_c,status,can_be_edited,can_manage_chat,can_change_info,can_post_messages,can_edit_messages,can_delete_messages,can_invite_users,can_restrict_members,can_promote_members,can_manage_voice_chats,is_anonymous)
    #print("\n\n", query, "\n\n")
    cur.execute(query)
    con.commit()
    con.close()
