import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    all_characters = letters + digits + punctuation
    password = ''.join(random.choices(all_characters, k=length))
    return password
