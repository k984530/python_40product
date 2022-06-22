import qrcode

qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

save_path = 'P04QR코드생성\\' + qr_data + '.png'

qr_img.save(save_path)