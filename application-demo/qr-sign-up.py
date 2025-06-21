import os
import qrcode

#img = qrcode.make("https://tinyurl.com/summer2021-code-camp-signup")
img_summer_2022 = qrcode.make("tinyurl.com/summercodingcamp2022")
img_signup = qrcode.make("https://forms.gle/tpArCcbZCaxpKfpK6")
img_summer_2022.save("qr_summer_2022_coding.png", "PNG")
img_signup.save("qr_summer_2022_signup.png", "PNG")
os.system("open qr_summer_2022_signup.png")
