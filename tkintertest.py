from tkinter import *
import string, random
password = "--------"

def on_click():
    chars = string.ascii_letters + string.digits
    password = "".join(random.sample(chars, 8))
    label.config(text=password)

def copy_text():
    if label.cget("text") == "--------":
        label.config(text="Generate first!")
        root.after(900, restore)
        return
    root.clipboard_clear()
    root.clipboard_append(label.cget("text"))
    root.update()
    label.config(text="Copied!")
    root.after(900, restore)

def restore():
    label.config(text=password)

root = Tk()
root.title("Random Password Generator")
root.geometry("300x200")
root.config(bg="skyblue")

frame = Frame(root, padx=15, pady=15)
frame.pack(fill="both", expand=True, padx=10, pady=10)

Label(frame, text="Password Here:").pack(pady=5)

label = Label(frame, text="--------", font=("Arial", 14))
label.pack(pady=10)

button = Button(frame, text="Generate Password", command=on_click)
button.pack(pady=5)
button2 = Button(frame, text="Click to Copy", command=copy_text,)
button2.pack(pady=5)

root.mainloop()
