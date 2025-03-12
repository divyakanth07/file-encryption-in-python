Sure! Here's the updated `README.md` with the inclusion of `better_encryption.py` and details on its functionality:


# File Encryption in Python

This is a Python project that demonstrates file encryption and decryption using two different encryption methods:
1. **Fernet Encryption**: A symmetric encryption technique (same key for encryption and decryption).
2. **AES + RSA Hybrid Encryption**: A more advanced method combining **RSA** (asymmetric encryption) for encrypting the AES key and **AES** (symmetric encryption) for encrypting the file contents.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Fernet Encryption](#fernet-encryption)
  - [AES + RSA Hybrid Encryption](#aes--rsa-hybrid-encryption)
- [How It Works](#how-it-works)
  - [Fernet Encryption](#fernet-encryption)
  - [AES + RSA Hybrid Encryption](#aes--rsa-hybrid-encryption)
- [License](#license)

## Introduction

This repository contains Python scripts for encrypting and decrypting files using two distinct encryption methods:

1. **Fernet Encryption**: This is a symmetric encryption technique where the same key is used for both encryption and decryption.
2. **AES + RSA Hybrid Encryption**: This method uses asymmetric RSA encryption for encrypting the AES key and symmetric AES encryption for encrypting the file's data. It provides better security by combining both encryption techniques.

## Installation

To run the encryption scripts, you'll need Python installed along with the following libraries:

- `cryptography` (for Fernet encryption)
- `pycryptodome` (for AES and RSA encryption)

You can install them using `pip`:

```bash
pip install cryptography pycryptodome
```

## Usage

### Fernet Encryption

The `simple_encryption.py` script demonstrates how to encrypt and decrypt files using **Fernet** symmetric encryption.

1. **Generate the Encryption Key**: The script generates an encryption key and stores it in a file (`filekey.key`).
2. **Encrypt a File**: It reads an input file (e.g., `test.txt`), encrypts it using the key, and writes the encrypted data to a new file (`encryptedfile`).
3. **Decrypt the File**: The script demonstrates how to decrypt the encrypted file and save the decrypted content into a new file (`decryptedfile`).

### AES + RSA Hybrid Encryption

The `better_encryption.py` script demonstrates a more advanced **AES + RSA Hybrid Encryption** technique. In this method:

- **RSA encryption** is used to encrypt the AES key (a symmetric key).
- **AES encryption** is used to encrypt the actual file data.

This method is more secure as it combines both asymmetric and symmetric encryption.

1. **Encrypt a File**: The script generates a random AES key, encrypts it using RSA, then uses AES to encrypt the file contents.
2. **Decrypt a File**: The script decrypts the AES key using RSA, then decrypts the file contents using AES.

### File Names and Extensions

- **test.txt**: The file you want to encrypt.
- **encryptedfile**: The file containing the encrypted content.
- **decrypted_test.txt**: The file containing the decrypted content.
- **rsakey.txt**: The file containing the RSA private/public key used for encryption/decryption.

## How It Works

### Fernet Encryption
1. **Generate a Key**: The script generates a key that is saved to a file (`filekey.key`).
2. **Encrypt and Decrypt Files**: It encrypts a file using the key, and decrypts it using the same key.

### AES + RSA Hybrid Encryption
1. **Generate AES Key**: A random 256-bit AES key is generated to encrypt the file data.
2. **Encrypt the AES Key**: The AES key is encrypted using RSA encryption.
3. **Encrypt the File**: The file data is encrypted using AES (with the encrypted AES key).
4. **Decrypt the File**: The AES key is decrypted using RSA, and then the file data is decrypted using AES.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
### What's New:
- I've added sections for the AES + RSA Hybrid Encryption (i.e., `better_encryption.py`).
- The "Usage" section now describes both the Fernet encryption and AES + RSA encryption methods.
- Detailed code explanations and usage instructions are provided for both scripts.