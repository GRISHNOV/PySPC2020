from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from .crypto_lib import *
from .s_box_lib import *
import time


class AppMainWindow:
    def __init__(self, master):
        """Service GUI sector"""
        frame = Frame(master)
        frame.pack()
        frame_password = LabelFrame(master, text="PASSWORD", padx=5, pady=5)
        frame_password.pack()
        # Help and Exit buttons
        self.button = Button(frame, text="EXIT", fg="red", width=15, height=2, background='yellow', command=frame.quit)
        self.button.pack(side=RIGHT, padx=25, pady=25)
        self.button = Button(frame, text="HELP", fg="orange", width=15, height=2, background='grey',
                             command=self.showHelp)
        self.button.pack(side=RIGHT, padx=25, pady=25)
        # Password input area
        self.input_password = Entry(frame_password, width=50)
        self.input_password.pack(padx=10, pady=10)
        # Decrypt file button
        self.b2 = Button(text="Decrypt file on disk", command=self.decryptFile)
        self.b2.pack(side=BOTTOM, padx=25, pady=25)
        # Encrypt file button
        self.b2 = Button(text="Encrypt file on disk", command=self.encryptFile)
        self.b2.pack(side=BOTTOM, padx=25, pady=25)


    def showHelp(self):
        """Show user help"""
        messagebox.showinfo('Help', 'Description')


    def encryptFile(self):
        """Encryption user file on disk"""
        user_key = str(self.input_password.get())
        if user_key == '':
            messagebox.showerror('Error', 'Password can not be empty')
            return
        input_filename = filedialog.askopenfilename()
        output_filename = input_filename + '.encrypted'
        fd_input = open(input_filename, "rb")
        fd_output = open(output_filename, "wb")
        # TODO: IV <- get with good entropy
        iv = time.time_ns()
        gamma = get_sha512(user_key)
        encrypt_file(fd_input, fd_output, user_key, iv)  # TODO: process return code
        fd_input.close()
        fd_output.close()
        messagebox.showinfo('Information', 'Encryption completed')


    def decryptFile(self):
        """Decryption user file on disk"""
        user_key = str(self.input_password.get())
        if user_key == '':
            messagebox.showerror('Error', 'Password can not be empty')
            return
        input_filename = filedialog.askopenfilename()
        output_filename = input_filename[:len(input_filename)-len('.encrypted')]  # TODO: check input format
        fd_input = open(input_filename, "rb")
        fd_output = open(output_filename, "wb")
        decrypt_file(fd_input, fd_output, user_key)  # TODO: process return code
        fd_input.close()
        fd_output.close()
        messagebox.showinfo('Information', 'Decryption completed')


if __name__ == "__main__":
    pass
