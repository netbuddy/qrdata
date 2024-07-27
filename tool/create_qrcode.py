import qrcode
import sys

def generate_qr_code_from_file(file_path):
    qr = qrcode.QRCode(
        version=40,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    with open(file_path, 'r') as file:
        # data = file.read().replace('\n', '')
        data = file.read()
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    qr_image = generate_qr_code_from_file(file_path)
    qr_image.save("qr_code.png")
    print("QR code saved to qr_code.png")