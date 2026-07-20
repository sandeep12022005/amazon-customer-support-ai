chat_memory = {}


def get_history(session_id):

    return chat_memory.get(session_id, [])


def add_message(session_id, role, message):

    if session_id not in chat_memory:
        chat_memory[session_id] = []

    chat_memory[session_id].append(
        {
            "role": role,
            "message": message
        }
    )


def build_history(session_id):

    history = ""

    for msg in get_history(session_id):

        history += f"{msg['role']}: {msg['message']}\n"

    return history