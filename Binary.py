#Decimal to Binary Conversion
while True:
 dec = 0
 binary_num = 0
 decimal_num = 0
 print("Decimal to Binary Conversion")
 dec=int(input("Type a decimal number: "))
 def bin2dec(binary):
     dec = int(str(binary), 2)
     return dec

 def dec2bin(decimal):
     bina = ""
     bin(dec)
     bina = int(bin(decimal)[2:])
     return bina
 decimal_num = dec2bin(dec)
 binary_num = bin2dec(decimal_num)
 print("Decimal Number: {}" .format(binary_num))
 print("Binary Number: {}" .format(decimal_num))