from cryptography.fernet import Fernet

def encrypt_data(data, key):
    """Encrypt data using AES-256 encryption."""
    cipher = Fernet(key)
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data, key):
    """Decrypt data using AES-256 encryption."""
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_data.encode()).decode()