import random
import string

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

BASE62_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62_CHARS[0]

    base = len(BASE62_CHARS)
    result = []

    while num > 0:
        result.append(BASE62_CHARS[num % base])
        num //= base

    return "".join(reversed(result))