import tkinter as tk
from tkinter import messagebox

class PlaylistGUI(tk.Tk):

    def submit_data(self, uid_var, api_var):
        messagestring = "Your UID is: " + uid_var.get() + "\nYour API key is: " + api_var.get() + "\nFunctionality isn't implemented yet :("
        messagebox.showinfo(title="Data Submission", message=messagestring)
    
    def create_main_page(self):

        uid_var = tk.StringVar()
        api_var = tk.StringVar()

        uid_label = tk.Label(self, text="Please enter your user ID")
        uid_label.pack(pady=10)

        uid_entry = tk.Entry(self, textvariable=uid_var)
        uid_entry.pack(pady = 10)

        api_label = tk.Label(self, text="Please enter your API key")
        api_label.pack(pady=10)

        api_entry = tk.Entry(self, textvariable=api_var)
        api_entry.pack(pady = 10)

        sub_button = tk.Button(self, text="Submit", command =lambda: self.submit_data(uid_var, api_var))
        sub_button.pack(pady=10)

    def __init__(self):
        super().__init__()
        self.title("Spotify Playlist Builder")
        self.geometry("300x250")
        self.create_main_page()

if __name__ == "__main__":
    app = PlaylistGUI()
    app.mainloop()