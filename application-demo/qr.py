import os
import qrcode

img = qrcode.make("https://www.facebook.com/FireKirinFLL/")
img.save("qr.png", "PNG")
os.system("open qr.png")
