# AICTE_Project

Overview:
This project implements an image steganography application using Tkinter for the GUI and OpenCV for image processing. It allows users to hide messages within an image and later extract the hidden message using a password.

Encryption: A message is embedded into an image by modifying the least significant bit (LSB) of the pixel values.
Decryption: The hidden message is retrieved from the image, provided the correct password is entered.
The application includes two main windows:

Encryption Window: Used to hide messages in an image.
Decryption Window: Used to extract hidden messages from an encrypted image.

Features:
Encrypt a message: Input a message and an image, then hide the message in the image.
Password protection: A password is required to encrypt and decrypt the message. The password must be at least 8 characters long.
Decrypt a message: Given an image with a hidden message and the correct password, the hidden message can be extracted.
File format support: The application supports PNG, JPG, and JPEG image formats.

Requirements:
Before running the application, ensure you have the following dependencies installed:
1. Python 3.x
2. Tkinter
3. OpenCV (cv2)
4. NumPy

You can install the required libraries with the following command:
pip install opencv-python

Code Structure:
encrypt.py:
This file contains the GUI and functionality to encrypt a message within an image.

1. encrypt_message_in_image(): Embeds the message into the image.
2. browse_image(): Allows the user to select an image.
3. encrypt(): Initiates the encryption process.

decrypt.py:
This file contains the GUI and functionality to decrypt a message from an image.

1. decrypt_message_from_image(): Extracts the hidden message from the image.
2. browse_image(): Allows the user to select the encrypted image.
3. decrypt(): Initiates the decryption process.

Troubleshooting:
1. Password Not Found: If the password file is missing, you may need to regenerate the encrypted image.
2. Incorrect Password: Make sure the password you entered matches the one used for encryption.
3. Message Not Found: If the message doesn't decrypt properly, verify that the image you selected is the correct encrypted image.
