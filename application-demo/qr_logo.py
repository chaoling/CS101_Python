import qrcode
from PIL import Image

def generate_colored_qr_with_logo(data, logo_path, qr_color='black', bg_color=(255, 255, 255, 0), logo_size_percent=15, qr_size=500):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=qr_color, back_color=bg_color)

    logo = Image.open(logo_path).convert("RGBA")
    logo_width = qr_img.size[0] * logo_size_percent // 100
    logo_height = qr_img.size[1] * logo_size_percent // 100
    logo_resized = logo.resize((logo_width, logo_height))

    qr_position = ((qr_img.size[0] - logo_width) // 2, (qr_img.size[1] - logo_height) // 2)
    qr_img.paste(logo_resized, qr_position, logo_resized)

    return qr_img

# Example usage

data = "http://www.youtube.com/@charlesling007"
logo_path = "Youtube-Icon-square.png"  # Replace with the path to your logo image
qr_color = 'white' # Choose the color for the QR code
bg_color = None  # Choose the background color
qr_with_logo = generate_colored_qr_with_logo(data, logo_path, qr_color, bg_color)
qr_with_logo.show()  # Display the colored QR code with logo
qr_with_logo.save("qr_youtube_logo.png")  # Save the QR code with logo to a file


# Example usage
'''
data = "https://facebook.com/FireKirinFLL"
logo_path = "fbook.png"  # Replace with the path to your logo image
qr_with_logo = generate_colored_qr_with_logo(data, logo_path, qr_color='white', bg_color=None)
qr_with_logo.show()  # Display the QR code with logo
qr_with_logo.save("qr_facebook_logo.png")  # Save the QR code with logo to a file
'''

