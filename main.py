# Importing functions from other files
from encryption_utils import generate_key, encrypt_message, decrypt_message
from file_manager import load_password_store, save_password_store
from auth import hash_password, check_password
from utils import generate_password
from password_manager import add_password, get_password, update_password, delete_password, search_password, categorize_password

def main():
    # Initialize password store and encryption key
    password_store = load_password_store(file_path="password_store.json")
    encryption_key = generate_key()

    # Simple master password check (for demonstration; in a real application, this would be more secure)
    master_password = "123"
    hashed_master_password = hash_password(master_password)

    entered_password = input("Enter the master password to unlock the password manager: ")
    if not check_password(entered_password, hashed_master_password):
        print("Incorrect master password. Exiting.")
        return

    while True:
        print("\nWelcome to the Advanced Password Manager!")
        print("Please choose an option:")
        print("1. Add a new password")
        print("2. Retrieve a stored password")
        print("3. Update an existing password")
        print("4. Delete a password")
        print("5. Generate a strong password")
        print("6. Search for a password entry")
        print("7. Categorize a password entry")
        print("8. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_password(service, username, password, encryption_key, password_store)
            print(f"Password added for {service}.")

        elif choice == "2":
            service = input("Enter the service name: ")
            username, password = get_password(service, encryption_key, password_store)
            if username and password:
                print(f"Username: {username}\nPassword: {password}")
            else:
                print("No entry found.")

        elif choice == "3":
            service = input("Enter the service name: ")
            new_password = input("Enter the new password: ")
            update_password(service, new_password, encryption_key, password_store)
            print(f"Password updated for {service}.")

        elif choice == "4":
            service = input("Enter the service name: ")
            delete_password(service, password_store)
            print(f"Password deleted for {service}.")

        elif choice == "5":
            length = int(input("Enter the desired length for the strong password: "))
            strong_password = generate_password(length)
            print(f"Generated strong password: {strong_password}")

        elif choice == "6":
            service = input("Enter the service name: ")
            entry = search_password(service, password_store)
            print(f"Entry for {service}: {entry}")

        elif choice == "7":
            service = input("Enter the service name: ")
            category = input("Enter the category: ")
            categorize_password(service, category, password_store)
            print(f"Entry categorized under {category}.")

        elif choice == "8":
            print("Exiting the password manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

        # Save changes to password store after every operation
        save_password_store(password_store, file_path="password_store.json")

# To run the program, you would simply call main() in your local environment
if __name__ == '__main__':
    main()
