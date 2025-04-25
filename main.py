import qrcode
from PIL import Image

# WhatsApp link
wa_link = input("Enter your encoded URL: ")
file_name = input("Enter the file name to save the QR code (without extension) (e.g. qr_youtube): ")

# Generate QR code
qr = qrcode.make(wa_link)

# Save and show the QR code
qr_path = f"results/{file_name}.png"
qr.save(qr_path)
