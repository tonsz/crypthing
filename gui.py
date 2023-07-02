import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox
import crypthing

# The interface of the Program. 
# Using tkinter, down below we created a Class 
# that constitute buttons, labels and stuff
# Everything about the GUI


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Crypthing!")
        self.window.geometry("370x450")
        self.window.configure(padx=20, pady=20, bg="#2e2e2e") 

        # Welcome banner
        welcome = tk.Label(self.window, text="Welcome to Crypthing: Encrypt and Decrypt!", pady="10",  bg="#2e2e2e", fg="white", font="Roboto")
        welcome.grid(row=0, column=0, columnspan=2)

        # Encrypt o Decrypt? pera o bayong
        self.radio_var = tk.StringVar(value="encrypt")

        self.radio_encrypt = ctk.CTkRadioButton(self.window, text="Encrypt", variable=self.radio_var, value="encrypt")
        self.radio_encrypt.grid(row=1, column=0)

        self.radio_decrypt = ctk.CTkRadioButton(self.window, text="Decrypt", variable=self.radio_var, value="decrypt")
        self.radio_decrypt.grid(row=1, column=1)

        self.radio_var.trace('w', self.on_radio_changed)

        # Enter key label and input
        self.key_label = tk.Label(self.window, text="ENTER KEY:", fg="white", bg="#2e2e2e", pady=15)
        self.key_entry = ctk.CTkEntry(self.window, show="*")
        

        # Upload file button
        open_button = ctk.CTkButton(self.window, text="Upload File", command=self.open_file_dialog)
        open_button.grid(row=3, column=0, columnspan=2, pady=12, padx=10)
        

        # Process file button
        self.process_button = ctk.CTkButton(self.window, text="Process File", command=self.process_file, state="disabled")
        self.process_button.grid(row=4, column=0, columnspan=2)

        # Create a label to display the selected file path or status
        self.file_path_var = tk.StringVar()
        label = tk.Label(self.window, textvariable=self.file_path_var, bg="#2e2e2e", fg="white", pady=15)
        label.grid(row=5, column=0, columnspan=2)

    # Function for changing the look
    def on_radio_changed(self, *args):
        selection = self.radio_var.get()

        if selection == "decrypt":
            self.key_label.grid(row=2, column=0)
            self.key_entry.grid(row=2, column=1)
        elif selection == "encrypt":
            self.key_label.grid_forget()
            self.key_entry.grid_forget()
        
    def open_file_dialog(self):
        filepath = filedialog.askopenfilename()
        if filepath:
            if not filepath.endswith(".txt"):
                self.file_path_var.set(filepath)
                messagebox.showerror("Error", "File is not a .txt file")
                self.process_button.configure(state="disabled")
            else:
                self.file_path_var.set(filepath)
                self.process_button.configure(state="normal")

    def process_file(self):
        source_file = self.file_path_var.get()
        if not source_file:
            return

        selection = self.radio_var.get()

        if selection == "decrypt":
                # prompt if user wanted to continue to encrypt the txt file
                answer = messagebox.askquestion("Are you sure?", "Are you sure you want to continue?", icon = 'question')
                # if yes, execute the following command
                if answer == 'yes':
                    crypthing.decrypt_file(source_file, self.file_path_var, self.key_entry.get())
        elif selection == "encrypt":
                # prompt if user wanted to continue to encrypt the txt file
                answer = messagebox.askquestion("Are you sure?", "Are you sure you want to continue?", icon = 'question')
                # if yes, execute the following command
                if answer == 'yes':
                    crypthing.encrypt_file(source_file, self.file_path_var)

    def run(self):
        self.window.mainloop()
