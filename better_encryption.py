import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def encrypt_file(rsa, input_path, output_path):
    secret_key = get_random_bytes(32)

    cipher_rsa = PKCS1_OAEP.new(rsa)
    encrypted_secret_key = cipher_rsa.encrypt(secret_key)
    
    with open(output_path, 'wb') as output:
        output.write(len(encrypted_secret_key).to_bytes(4, byteorder='big'))
        output.write(encrypted_secret_key)

        iv = get_random_bytes(16)
        aes_engine = AES.new(secret_key, AES.MODE_CBC, iv)
        output.write(iv)

        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()
            encrypted_data = aes_engine.encrypt(pad(input_data, AES.block_size))
            output.write(encrypted_data)

encrypt_file(RSA.generate(2048), 'test.txt', 'encryptedfile')
