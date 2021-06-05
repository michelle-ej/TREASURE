
import zxing
reader = zxing.BarCodeReader()

#這裡也是
barcode = reader.decode('1.jpg')

print(barcode.parsed)
