import tkinter as tk
from backend.wallet import Wallet

def recover():
    seed = entry.get()
    wallet = Wallet()
    result = wallet.recover_wallet(seed)
    result_label.config(text=result)

# UI setup
root = tk.Tk()
root.title("Recover Wallet")

entry = tk.Entry(root, width=50)
entry.pack()

recover_button = tk.Button(root, text="Recover Wallet", command=recover)
recover_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()