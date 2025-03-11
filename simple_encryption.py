from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('filekey.key', 'wb') as filekey:
	filekey.write(key)

with open('filekey.key', 'rb') as filekey:
	key = filekey.read()

fernetKey = Fernet(key)

with open('test.txt', 'rb')as testfile: #change the name of the file. It can encrypt any file with any extension
	original = testfile.read()

encrypted = fernetKey.encrypt(original)

with open('encryptedfile', 'wb') as encryptedfile:
	encryptedfile.write(encrypted)

with open('encryptedfile', 'rb') as encryptedfile:
	encryptedfile.read()

decrypted = fernetKey.decrypt (encrypted)

with open('decryptedfile', 'wb') as decryptedfile:
	decryptedfile.write(decrypted)

with open('decryptedfile', 'rb') as decryptedfile:
	decryptedfile.read()