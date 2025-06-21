import barcode
from barcode.writer import ImageWriter
from io import BytesIO

#cardnum = '1 2300 03093 574'
cardnum = '1 2500 03641 347'
savefilename='mcld_library_card_barcode_cl'
barcode_formats = barcode.PROVIDED_BARCODES
print(barcode_formats)
#code=barcode.get_barcode_class('code39')
for format in barcode_formats:
    try:
        code=barcode.get_barcode_class(format)
        mycard = code(cardnum, writer=ImageWriter())
        img = mycard.save(f'{savefilename}_{format}')
    except Exception as e:
        pass

#name = generate('EAN13', cardnum, no_checksum=True, output=savefilename)
 
#fp = BytesIO()
#generate('EAN13', cardnum, writer=ImageWriter(), output=fp)
