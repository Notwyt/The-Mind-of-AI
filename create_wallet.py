import tkinter as tk
from backend.wallet import Wallet

def generate_wallet():
    try:
        wallet = Wallet()
        seed_phrase = wallet.create_wallet()
        seed_label.config(text="Your Seed Phrase:\n" + seed_phrase)
    except Exception as e:
        seed_label.config(text="Error generating wallet:\n" + str(e))

# UI setup
root = tk.Tk()
root.title("Create Wallet")

seed_label = tk.Label(root, text="Click to generate wallet", padx=10, pady=10)
seed_label.pack()

generate_button = tk.Button(root, text="Generate Wallet", command=generate_wallet)
generate_button.pack()

root.mainloop()