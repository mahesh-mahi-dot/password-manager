import json
import base64

def load_password_store(file_path):
    try:
        with open(file_path, "r") as f:
            data = f.read()
            if not data:
                print("Warning: JSON file is empty. Returning an empty store.")
                return {}
            return json.loads(data)
    except FileNotFoundError:
        print("Warning: File not found. Returning an empty store.")
        return {}
    except json.JSONDecodeError:
        print("Warning: Could not decode the JSON file. Returning an empty store.")
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
