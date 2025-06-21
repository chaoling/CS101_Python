import pyqrcode
from PIL import Image

# Generate the qr code and save as png
qrobj = pyqrcode.create('https://facebook.com/GoldenPhoenixFLL')
with open('qr.png', 'wb') as f:
    qrobj.png(f, scale=10)

# Now open that png image to put the logo
img = Image.open('qr.png')
width, height = img.size

# How big the logo we want to put in the qr code png
logo_size = 100

# Open the logo image
logo = Image.open('fbook.png')

# Calculate xmin, ymin, xmax, ymax to put the logo
xmin = ymin = int((width / 2) - (logo_size / 2))
xmax = ymax = int((width / 2) + (logo_size / 2))

# resize the logo as calculated
logo = logo.resize((xmax - xmin, ymax - ymin))

# put the logo in the qr code
img.paste(logo, (xmin, ymin, xmax, ymax))

img.show()