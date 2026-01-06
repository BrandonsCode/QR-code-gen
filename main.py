import qrcode


def get_url():
    return input("Enter the URL of the QR code: ").strip()


def generate_qr_code(url):
    qr = qrcode.QRCode()
    qr.add_data(url)
    return qr.make_image()


def save_qr_code(img, file_path):
    img.save(file_path)


def main():
    try:
        url = get_url()
        file_path = "C:\\Users\\brand2\\Desktop\\qrcode.png"
        img = generate_qr_code(url)
        save_qr_code(img, file_path)
        print("QR code was generated!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
