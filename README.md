# File Encryption in Python

This is a simple Python script that demonstrates how to encrypt and decrypt files using the **Fernet** symmetric encryption algorithm from the `cryptography` library.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License](#license)

## Introduction

This project showcases how to securely encrypt and decrypt any file using Python. The encryption is achieved using the `cryptography` module's `Fernet` class, which ensures the encryption is safe and symmetric (same key is used for both encryption and decryption).

## Installation

To use this encryption script, make sure you have Python installed. Then, you need to install the `cryptography` library.

To install the necessary dependencies, run the following command:

```bash
pip install cryptography
```

## Usage

1. **Generate the Encryption Key:**

   The script generates an encryption key (`filekey.key`) which is used for encryption and decryption. It writes this key into a file, so it can be used later for decryption.

2. **Encrypting a File:**

   The script reads an input file (e.g., `test.txt`), encrypts its contents, and writes the encrypted data to `encryptedfile`.

3. **Decrypting a File:**

   After encryption, the script demonstrates how to decrypt the `encryptedfile` and write the decrypted contents into a new file (`decryptedfile`).

## How It Works

1. **Generate a Key:** The encryption key is generated using `Fernet.generate_key()`. This key is saved to a file (`filekey.key`).

2. **Encrypt a File:** The script reads the contents of any file (you can change the file name in the code to target different files), encrypts them with the previously saved key, and writes the encrypted content to a new file.

3. **Decrypt the File:** The encrypted file is read and decrypted using the same key, resulting in the original content being restored.

### File Names and Extensions

- **test.txt**: The file you want to encrypt.
- **encryptedfile**: The file containing the encrypted content.
- **decryptedfile**: The file containing the decrypted content.
- **filekey.key**: The file containing the encryption key used for both encryption and decryption.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
