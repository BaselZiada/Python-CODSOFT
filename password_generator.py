import customtkinter as ctk
import random
import string
import pyperclip

def generate_password():
    length = int(length_slider.get())
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    character_set = ''
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation

    if character_set:
        password = ''.join(random.choice(character_set) for _ in range(length))
        password_var.set(password)
        check_password_strength(password)
    else:
        password_var.set("Please select character types")

def check_password_strength(password):
    strength = "Weak"
    if len(password) >= 12:
        strength = "Good"
    if len(password) >= 12 and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
        strength = "Strong"
    
    strength_var.set(f"Strength: {strength}")

def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    ctk.messagebox.showinfo("Copied", "Password copied to clipboard!")

def update_length_label(value):
    length_value_var.set(f"Length: {int(value)}")

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("green")  

app = ctk.CTk()
app.geometry("400x500")
app.title("Password Generator")

title_label = ctk.CTkLabel(app, text="Password Generator", font=("Arial", 24, "bold"))
title_label.pack(pady=20)


length_value_var = ctk.StringVar(value="Length: 32")
length_label_frame = ctk.CTkFrame(app)
length_label_frame.pack(pady=10)

length_label = ctk.CTkLabel(length_label_frame, textvariable=length_value_var)
length_label.pack(side="left", padx=10)

length_slider = ctk.CTkSlider(length_label_frame, from_=4, to=64, number_of_steps=60, command=update_length_label)
length_slider.set(32)  # Default length
length_slider.pack(side="right", padx=10)


icon_frame = ctk.CTkFrame(app)
icon_frame.pack(pady=10)

uppercase_icon = ctk.CTkLabel(icon_frame, text="A(a)-Z(z)", font=("Arial", 18, "bold"))
uppercase_icon.grid(row=0, column=0, padx=20)

digits_icon = ctk.CTkLabel(icon_frame, text="0-9", font=("Arial", 18, "bold"))
digits_icon.grid(row=0, column=2, padx=20)

special_icon = ctk.CTkLabel(icon_frame, text="#$%^", font=("Arial", 18, "bold"))
special_icon.grid(row=0, column=3, padx=20)


uppercase_var = ctk.BooleanVar(value=True)
lowercase_var = ctk.BooleanVar(value=True)
digits_var = ctk.BooleanVar(value=True)
special_var = ctk.BooleanVar(value=True)

switch_frame = ctk.CTkFrame(app)
switch_frame.pack(pady=20)

uppercase_switch = ctk.CTkSwitch(switch_frame, text="Include Uppercase", variable=uppercase_var)
uppercase_switch.grid(row=0, column=0, padx=20, pady=5, sticky="w")

lowercase_switch = ctk.CTkSwitch(switch_frame, text="Include Lowercase", variable=lowercase_var)
lowercase_switch.grid(row=1, column=0, padx=20, pady=5, sticky="w")

digits_switch = ctk.CTkSwitch(switch_frame, text="Include Numbers", variable=digits_var)
digits_switch.grid(row=2, column=0, padx=20, pady=5, sticky="w")

special_switch = ctk.CTkSwitch(switch_frame, text="Include Symbols", variable=special_var)
special_switch.grid(row=3, column=0, padx=20, pady=5, sticky="w")


generate_button = ctk.CTkButton(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)


password_var = ctk.StringVar()
password_entry = ctk.CTkEntry(app, textvariable=password_var, width=300, state="readonly")
password_entry.pack(pady=10)


strength_var = ctk.StringVar(value="Strength: ")
strength_label = ctk.CTkLabel(app, textvariable=strength_var)
strength_label.pack(pady=10)


copy_button = ctk.CTkButton(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

app.mainloop()
