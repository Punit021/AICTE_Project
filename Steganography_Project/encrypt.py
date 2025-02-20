import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np

def encrypt_message_in_image(image_path, message, password, output_image_path):
    with open("password.txt", "w") as password_file:
        password_file.write(password)
    
    img = cv2.imread(image_path)    
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  
    
    data_index = 0
    binary_length = len(binary_message)
    
    for row in img:
        for pixel in row:
            for channel in range(3): 
                if data_index < binary_length:
                    pixel[channel] = int(format(pixel[channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1

    cv2.imwrite(output_image_path, img)
    messagebox.showinfo("Success", f"Message hidden successfully! Encrypted image saved as {output_image_path}")

def validate_password(password):
    if len(password) < 8: 
        return False
    return True

def browse_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if filepath:
        image_path_entry.delete(0, tk.END)
        image_path_entry.insert(0, filepath)

def encrypt():
    message = message_entry.get()
    image_path = image_path_entry.get()
    password = password_entry.get()
    
    if not message or not image_path or not password:
        messagebox.showerror("Input Error", "Please enter a message, password, and select an image.")
        return

    output_image_path = "encrypted_image.png"  
    encrypt_message_in_image(image_path, message, password, output_image_path)

root = tk.Tk()
root.title("Image Steganography - Encryption")

tk.Label(root, text="Select Image File").pack(pady=10)
image_path_entry = tk.Entry(root, width=50)
image_path_entry.pack(pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_image)
browse_button.pack(pady=5)

tk.Label(root, text="Enter Message to Hide").pack(pady=10)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

tk.Label(root, text="Enter Password (Min 8 characters)").pack(pady=10)
password_entry = tk.Entry(root, width=50, show="*")
password_entry.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt Message", command=encrypt)
encrypt_button.pack(pady=20)

root.mainloop()
