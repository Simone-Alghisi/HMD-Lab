from IPython.display import display, Markdown


def display_conversation(messages, user_msg, assistant_msg):
    md = (
        "### Conversation\n\n"
        f"**System:** {messages[0]['content']}\n\n"
        f"**User:** {user_msg}\n\n"
        f"**Assistant:** {assistant_msg}"
    )
    display(Markdown(md))
