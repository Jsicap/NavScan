import segno

# Create a QR code with the data "Door_1" and enable error correction (boost_error)
qrcode = segno.make_qr("Door_1", boost_error=True)

# Create another QR code with the data "Door_2" and enable error correction (boost_error)
qrcode2 = segno.make_qr("Door_2", boost_error=True)

# Save the first QR code as "door1.png" with a scale of 50 (higher scale results in larger QR codes)
qrcode.save("door1.png", scale=50)

# Save the second QR code as "door2.png" with a scale of 50
qrcode2.save("door2.png", scale=50
