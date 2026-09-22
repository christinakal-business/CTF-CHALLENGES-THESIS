from Crypto.Cipher import AES
import os

# reads original image in binary read mode
with open("car.bmp", "rb") as f:
    data = f.read()

# extracts 54-byte header
header = data[:54]
# extract remaining data after byte index 54
pixels = data[54:]

# pads the pixels so it is a multiple of 16 (AES block size)
pad_len = 16 - (len(pixels) % 16)
# PKCS#7 padding
pixels += bytes([pad_len] * pad_len)

# generates a pseudorandom 16-byte (128-bit) symmetric encryption key
key = os.urandom(16)
# AES e ncryption tool that uses key in ECB mode
cipher = AES.new(key, AES.MODE_ECB)
# encyrpt pixel data
encrypted_pixels = cipher.encrypt(pixels)

# pads entire file so the total size is a multiple of 16 and encrypt it
encrypted_final = cipher.encrypt(data + bytes([16 - (len(data) % 16)] * (16 - (len(data) % 16))))

# opens new file ("encrypted_car.bin") to write binary data
with open("encrypted_car.bin", "wb") as f:
    f.write(encrypted_final)

print("Success!")