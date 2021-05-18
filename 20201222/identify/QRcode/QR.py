import qrcode

qr = qrcode.QRCode(version = 3, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10,border = 4)

'''
version: 一個1~40的整數，用來控制QR code的尺寸。最小的尺寸為一個21×21格的矩陣。若設定為None且make函數之fit參數為True時，將自動決定QR code的尺寸。
error_correction: 錯誤碼糾正程度，影響了QR code若被污損造成難以辨識，能自動修復的比例。
有四種程度可調整，分別為ERROR_CORRECT_L(7%可被修正)、ERROR_CORRECTION_M(15%可被修正)、ERROR_CORRECTION_Q(25%可被修正)、ERROR_CORRECTION_H(30%可被修正)，越大的修正程度將會佔用更多的資料空間。
box_size: 控制每個格子的像素數量，預設為10
border: 控制邊框包含的格子數量，預設為4，是標準規定的最小值。
image_factory: 用來控制生成的QR code圖檔型別。 (這邊沒用到)
'''

qr.add_data('https://line.me/ti/p/2bGHk_50ir') 
qr.make(fit = True)
 
img = qr.make_image()
img.save("QRcode.jpg")