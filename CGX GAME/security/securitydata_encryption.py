from cryptography.fernet import Fernet
import pickle
import os

def generate_key():
    """Generates a new encryption key."""
    key = Fernet.generate_key()
    return key

def encrypt_data(data, key):
    """Encrypts data using the provided key."""
    f = Fernet(key)
    encrypted_data = f.encrypt(pickle.dumps(data))
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """Decrypts data using the provided key."""
    f = Fernet(key)
    decrypted_data = pickle.loads(f.decrypt(encrypted_data))
    return decrypted_data

def encrypt_save_file(filename, key):
    """Encrypts a save file."""
    if not os.path.exists(filename):
        return False, "Save file does not exist."
    try:
        with open(filename, 'rb') as file:
            data = file.read()
        encrypted_data = encrypt_data(data, key)
        with open(filename, 'wb') as file:
            file.write(encrypted_data)
        return True, "Save file encrypted."
    except Exception as e:
        return False, f"Error encrypting save file: {e}"

def decrypt_save_file(filename, key):
    """Decrypts a save file."""
    if not os.path.exists(filename):
        return False, "Save file does not exist."
    try:
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = decrypt_data(encrypted_data, key)
        with open(filename, 'wb') as file:
            file.write(decrypted_data)
        return True, "Save file decrypted."
    except Exception as e:
        return False, f"Error decrypting save file: {e}"
