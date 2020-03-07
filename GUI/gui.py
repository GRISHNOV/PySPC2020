from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


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
        # Encrypt file button
        self.b2 = Button(text="Encrypt file on disk", command=self.encryptFile)
        self.b2.pack(side=BOTTOM, padx=25, pady=25)
        # Select file button
        self.b1 = Button(text="Select file on disk", command=self.selectFile)
        self.b1.pack(side=BOTTOM, padx=25, pady=25)


    def showHelp(self):
        messagebox.showinfo('Help', 'Description')


    def encryptFile(self):
        file_name = filedialog.askopenfilename()
        f = open(file_name)
        # TODO: file encryption processing
        f.close()


    def selectFile(self):
        file_name = filedialog.asksaveasfilename(filetypes=(("TXT files", "*.txt"), ("HTML files", "*.html;*.htm"), ("All files", "*.*")))
        f = open(file_name, 'w')
        # TODO: selection files processing
        f.close()


if __name__ == "__main__":
    print("INFO: Open GUI")
    root = Tk()
    app_service_sector = AppMainWindow(root)
    root.mainloop()
    # root.destroy()
    print("INFO: Close GUI")