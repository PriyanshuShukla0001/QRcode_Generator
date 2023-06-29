import qrcode as qr

link=input("Enter the link")
img= qr.make(link)

pic=input("Enter the name of png file")
img.save(pic+".png")

print(f"QR code is generated.")
