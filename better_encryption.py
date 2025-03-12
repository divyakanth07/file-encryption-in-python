import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

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

def decrypt_file(rsa, input_path, output_path):
    with open(input_path, 'rb') as input_file:
        encrypted_key_len = int.from_bytes(input_file.read(4), byteorder='big')
        encrypted_secret_key = input_file.read(encrypted_key_len)

        cipher_rsa = PKCS1_OAEP.new(rsa)
        secret_key = cipher_rsa.decrypt(encrypted_secret_key)

        iv = input_file.read(16)
        aes_engine = AES.new(secret_key, AES.MODE_CBC, iv)

        encrypted_data = input_file.read()
        decrypted_data = unpad(aes_engine.decrypt(encrypted_data), AES.block_size)

        with open(output_path, 'wb') as output_file:
            output_file.write(decrypted_data)

def save_rsa_key(rsa, key_path):
	with open(key_path, 'wb') as key_file:
		key_file.write(rsa.export_key())

rsa_key = RSA.generate(2048)
encrypt_file(rsa_key, 'test.txt', 'encryptedfile')
decrypt_file(rsa_key, 'encryptedfile', 'decrypted_test.txt')
save_rsa_key(rsa_key, 'rsakey.txt')