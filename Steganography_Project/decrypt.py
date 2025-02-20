import tkinter as tk
from tkinter import filedialog, messagebox
import cv2

def decrypt_message_from_image(image_path, password):
   
    try:
        with open("password.txt", "r") as password_file:
            stored_password = password_file.read().strip()
    except FileNotFoundError:
        messagebox.showerror("Password Error", "Password file not found!")
        return ""
    
    if password != stored_password:
        messagebox.showerror("Password Error", "Incorrect password!")
        return ""

    binary_message = ""
    
    
    img = cv2.imread(image_path)
    for row in img:
        for pixel in row:
            for channel in range(3):  
                binary_message += format(pixel[channel], '08b')[-1] 

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '11111111': 
            break
        message += chr(int(byte, 2))
    return message

def validate_password(password):
    if len(password) < 8:  
        return False
    return True

def browse_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if filepath:
        image_path_entry.delete(0, tk.END)
        image_path_entry.insert(0, filepath)

def decrypt():
    image_path = image_path_entry.get()
    password = password_entry.get()
    if not image_path or not password:
        messagebox.showerror("Input Error", "Please select an image and enter the password.")
        return
    
    message = decrypt_message_from_image(image_path, password)
    if message: 
        messagebox.showinfo("Decrypted Message", f"Hidden message: {message}")
    else:
        messagebox.showerror("Decryption Error", "Failed to decrypt the message or incorrect password.")

root = tk.Tk()
root.title("Image Steganography - Decryption")

tk.Label(root, text="Select Encrypted Image File").pack(pady=10)
image_path_entry = tk.Entry(root, width=50)
image_path_entry.pack(pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_image)
browse_button.pack(pady=5)

tk.Label(root, text="Enter Password (Min 8 characters)").pack(pady=10)
password_entry = tk.Entry(root, width=50, show="*")  
password_entry.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt Message", command=decrypt)
decrypt_button.pack(pady=20)

root.mainloop()
