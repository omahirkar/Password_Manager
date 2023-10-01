from winreg import LoadKey
from cryptography.fernet import Fernet

from cryptography.fernet import Fernet
import os

# Generate or load the encryption key
def load_or_generate_key(key_file):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as file:
            key = file.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as file:
            file.write(key)
    return key

# Encrypt the password
def encrypt_password(key, password):
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Decrypt the password
def decrypt_password(key, encrypted_password):
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

# Save account details to a file
def save_account_details(file_name, account_name, encrypted_password):
    with open(file_name, 'a') as file:
        file.write(f"{account_name}: {encrypted_password}\n")

# View account details
def view_account_details(file_name, key):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            account_name, encrypted_password = line.strip().split(': ')
            decrypted_password = decrypt_password(key, encrypted_password)
            print(f"Account: {account_name}, Password: {decrypted_password}")

if __name__ == "__main__":
    key_file = "encryption_key.key"
    data_file = "passwords.txt"

    key = load_or_generate_key(key_file)

    while True:
        print("\nOptions:")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_name = input("Enter account name: ")
            password = input("Enter password: ")
            encrypted_password = encrypt_password(key, password)
            save_account_details(data_file, account_name, encrypted_password)
            print("Account details saved successfully.")

        elif choice == "2":
            view_account_details(data_file, key)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


# def load_key(file_path):
#     with open(file_path, "rb") as file:
#         key = file.read()
#     return key

# Specify the path to your key file
# key_file_path = "key.key"

# Load the key from the file
# key = load_key(key_file_path)

# def view():
#     with open('passwords.txt', 'r') as f:
#         for line in f.readlines():
#             data = line.rstrip()
#             user, passw = data.split("|")
#             print("User:", user, "| Password:",
#                   fer.decrypt(passw.encode()).decode())


# def add():
#     name = input('Account Name: ')
#     pwd = input("Password: ")

#     with open('passwords.txt', 'a') as f:
#         f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


# while True:
#     mode = input(
#         "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
#     if mode == "q":
#         break

#     if mode == "view":
#         view()
#     elif mode == "add":
#         add()
#     else:
#         print("Invalid mode.")
#         continue