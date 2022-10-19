import string
import secrets

def generate_pw(length: int, lowercase: bool, uppercase: bool, numbers: bool,
                symbols: bool, spaces: bool):
    selectionpool = ""

    if lowercase:
        selectionpool += string.ascii_lowercase
    if uppercase:
        selectionpool += string.ascii_uppercase
    if numbers:
        selectionpool += string.digits
    if symbols:
        selectionpool += string.punctuation
    if spaces:
        selectionpool += "      "

    selectionpool_length = len(selectionpool)
    password = ""

    for _ in range(length):
        password += selectionpool[secrets.randbelow(selectionpool_length)]

    return password

