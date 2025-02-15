from mnemonic import Mnemonic
from cryptography.fernet import Fernet
import os
import json

class Wallet:
    def __init__(self):
        self.mnemo = Mnemonic("english")

    def create_wallet(self, words=12):
        """Generate a new wallet with a BIP-39 mnemonic phrase."""
        seed_phrase = self.mnemo.generate(strength=128 if words == 12 else 256)
        return seed_phrase

    def save_wallet(self, seed_phrase, password):
        """Encrypt and save wallet data locally."""
        encryption_key = Fernet.generate_key()
        cipher = Fernet(encryption_key)
        encrypted_data = cipher.encrypt(seed_phrase.encode())

        # Save locally (replace with secure storage method)
        with open("wallet_data.json", "w") as file:
            json.dump({"encrypted_seed": encrypted_data.decode()}, file)

        return encryption_key

    def recover_wallet(self, seed_phrase):
        """Recover a wallet from a given seed phrase."""
        if self.mnemo.check(seed_phrase):
            return "Wallet successfully recovered!"
        else:
            return "Invalid seed phrase. Please check again."