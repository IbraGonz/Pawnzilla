import random


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hello there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`The ability to speak does not make you intelligent.`"

    return "`Pawns are the best Chess piece!`"
