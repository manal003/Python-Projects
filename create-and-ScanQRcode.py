import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version =1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size=10, border = 4)
qr.add_data('https://github.com/manal003/Manal')
qr.make(fit=True)
image = qr.make_image(fill_color= 'black', back_color='white')
image.save('C:\\Users\\Atif\\Documents\\Python\\QR_code\\myGitHub.png')
image.show()


