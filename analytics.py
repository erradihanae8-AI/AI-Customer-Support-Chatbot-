import datetime

LOG_FILE = "conversations.log"

def log_conversation(user_msg, bot_msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"[{datetime.datetime.now()}]\n"
            f"User: {user_msg}\n"
            f"Bot: {bot_msg}\n\n"
        )
