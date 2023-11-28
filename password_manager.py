from encryption_utils import encrypt_message
from encryption_utils import decrypt_message

import json
import base64

def load_password_store(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_password_store(store, file_path):
    new_store = {}
    for service, details in store.items():
        new_details = {}
        for k, v in details.items():
            if isinstance(v, bytes):
                new_details[k] = base64.urlsafe_b64encode(v).decode('utf-8')
            else:
                new_details[k] = v
        new_store[service] = new_details

    with open(file_path, "w") as f:
        json.dump(new_store, f)

def add_password(service, username, password, encryption_key, password_store):
    encrypted_password = encrypt_message(password, encryption_key)
    password_store[service] = {'username': username, 'password': encrypted_password}

def get_password(service, encryption_key, password_store):
    if service in password_store:
        encrypted_password = password_store[service]['password']
        decrypted_password = decrypt_message(encrypted_password, encryption_key)
        return password_store[service]['username'], decrypted_password
    else:
        return None, None

def update_password(service, new_password, encryption_key, password_store):
    if service in password_store:
        encrypted_new_password = encrypt_message(new_password, encryption_key)
        password_store[service]['password'] = encrypted_new_password

def delete_password(service, password_store):
    if service in password_store:
        del password_store[service]

def search_password(service, password_store):
    return password_store.get(service, "No entry found")

def categorize_password(service, category, password_store):
    if service in password_store:
        password_store[service]['category'] = category
