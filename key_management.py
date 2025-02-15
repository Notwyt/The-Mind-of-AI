import qrcode
import json

def generate_qr(seed_phrase):
    """Generate a QR code from the encrypted seed phrase."""
    qr = qrcode.make(seed_phrase)
    qr.save("wallet_qr.png")
    return "QR code saved as wallet_qr.png"

def scan_qr(qr_code_path):
    """Scan a QR code to import a seed phrase."""
    from pyzbar.pyzbar import decode
    from PIL import Image
    decoded_data = decode(Image.open(qr_code_path))
    if decoded_data:
        return decoded_data[0].data.decode()
    return "QR code not readable."