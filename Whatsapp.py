import tkinter as tk
import pywhatkit
import datetime
from datetime import timedelta

class GUI:
    def __init__(self):
        self.frame = tk.Tk()
        self.frame.geometry('400x300')
        self.frame.title("Send WhatsApp Message")
        
        # Label
        self.label = tk.Label(self.frame, text="Select Contact")
        self.label.pack(pady=10)

        # Dropdown menu for contact selection
        self.contact_options = ["Aditya", "Arafat", "Priyanshu", "Jayesh"]
        self.contact_var = tk.StringVar(self.frame)
        self.contact_var.set(self.contact_options[0])
        self.contact_dropdown = tk.OptionMenu(self.frame, self.contact_var, *self.contact_options)
        self.contact_dropdown.pack()

        # Textbox for message
        self.message_label = tk.Label(self.frame, text="Enter Message:")
        self.message_label.pack(pady=10)
        self.message_textbox = tk.Text(self.frame, height=5)
        self.message_textbox.pack()

        # Button to send message
        self.send_button = tk.Button(self.frame, text="Send Message", command=self.send_message)
        self.send_button.pack(pady=10)

        self.frame.mainloop()

    def send_message(self):
        # Get selected contact
        contact = self.contact_var.get()

        # Get message from textbox
        message = self.message_textbox.get("1.0", "end-1c")

        # Send message using pywhatkit
        str_time = int(datetime.datetime.now().strftime("%H"))
        time = int((datetime.datetime.now()+timedelta(minutes=2)).strftime("%M"))

        if contact == "Aditya":
            pywhatkit.sendwhatmsg("+916353178377", message, time_hour=str_time, time_min=time)
        elif contact == "Arafat":
            pywhatkit.sendwhatmsg("+917066020465", message, time_hour=str_time, time_min=time)
        elif contact == "Priyanshu":
            pywhatkit.sendwhatmsg("+918401087744", message, time_hour=str_time, time_min=time)
        elif contact == "Jayesh":
            pywhatkit.sendwhatmsg("+919726634150", message, time_hour=str_time, time_min=time)
            
        self.label.config(text="Message sent successfully")

gui = GUI()
