import pyqrcode
from PIL import Image

url = pyqrcode.QRCode('https://www.facebook.com/FireKirinFLL',error = 'H')
url.png('qrcode_firekirin.png',scale=10)
im = Image.open('qrcode_firekirin.png')
im = im.convert("RGBA")
logo = Image.open('hope_logo_trans.png')
box = (155,155,315,315)
im.crop(box)
region = logo
region = region.resize((box[2] - box[0], box[3] - box[1]))
im.paste(region,box)
im.show()
im.save("qrcode_final.png")