import os 
import pyperclip
from cryptography.fernet import Fernet   
from tkinter import messagebox

def encrypt_file(source_file, file_path_var):

    key = Fernet.generate_key()
    crypthing = Fernet(key)
 
    # read the content
    with open(source_file, 'r') as file:
        plaintext = file.read()

    ciphertext = crypthing.encrypt(plaintext.encode())

    output_file = generate_output_file_path(source_file)

    # write a new file with an encrypted content 
    with open(output_file, 'w') as file:
        # manipulate content here oh
        file.write(str(ciphertext, 'utf8'))
        copy_key_to_clipboard(key)
        messagebox.showinfo("Successful", "File written successfully and key copied to your clipboard!")   
        file_path_var.set("")
    return True
     
def decrypt_file(source_file, file_path_var, key): 

    crypthing = Fernet(key)
 
    # read the content
    with open(source_file, 'r') as file:
        ciphertext = file.read()
    
    plaintext = crypthing.decrypt(ciphertext)

    with open(source_file + "_decrypted.txt", 'w') as file:
        # manipulate content here oh
        file.write(str(plaintext, 'utf8')) 
        messagebox.showinfo("Successful", "Content decrypted and File written successfully!")  
        file_path_var.set("")
    return True

# write the encrypted file in a different filename                                                               
def generate_output_file_path(source_file):
    file_name, file_ext = os.path.splitext(source_file)
    output_file = f"{file_name}_encrypted{file_ext}"
    return output_file

def copy_key_to_clipboard(encryption_key):
    pyperclip.copy(str(encryption_key, 'utf8'))
