import segno

qrcode = segno.make_qr("Door_1", boost_error = True)
qrcode2 = segno.make_qr("Door_2", boost_error = True)
qrcode.save("door1.png", scale=50)
qrcode2.save("door2.png", scale=50)