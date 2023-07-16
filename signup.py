from tkinter import *

def register():
    full_name = full_name_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    re_enter_password = re_enter_password_entry.get()
    phone_number = phone_number_entry.get()
    gender = gender_var.get()
    
    # Perform sign-up validation and registration logic here
    
    if password != re_enter_password:
        register_label.config(text="Passwords do not match", fg="red")
    elif len(password) < 8:
        register_label.config(text="Password must be 8 characters long", fg="red")
    else:
        register_label.config(text="Registration successful", fg="green")

# Create the GUI window
root = Tk()
root.title("Sign Up Page")
root.configure(bg="#F0F0F0")  # Set background color

# Create Header Label
header_label = Label(root, text="Sign Up", font=("Arial", 18), fg="#333333", bg="#F0F0F0")
header_label.pack(pady=20)

# Create Frame for Labels and Entry Fields
frame = Frame(root, bg="#F0F0F0")
frame.pack()

# Create Labels
full_name_label = Label(frame, text="Full Name:", font=("Arial", 12), fg="#666666", bg="#F0F0F0")
full_name_label.grid(row=0, column=0, padx=5, pady=5)

username_label = Label(frame, text="Username:", font=("Arial", 12), fg="#666666", bg="#F0F0F0")
username_label.grid(row=1, column=0, padx=5, pady=5)

password_label = Label(frame, text="Password:", font=("Arial", 12), fg="#666666", bg="#F0F0F0")
password_label.grid(row=2, column=0, padx=5, pady=5)

re_enter_password_label = Label(frame, text="Re-enter Password:", font=("Arial", 12), fg="#666666", bg="#F0F0F0")
re_enter_password_label.grid(row=3, column=0, padx=5, pady=5)

phone_number_label = Label(frame, text="Phone Number:", font=("Arial", 12), fg="#666666", bg="#F0F0F0")
phone_number_label.grid(row=4, column=0, padx=5, pady=5)

gender_label = Label(frame, text="Gender:", font=("Arial", 12), fg="#666666", bg="#F0F0F0")
gender_label.grid(row=5, column=0, padx=5, pady=5)

# Create Entry fields
full_name_entry = Entry(frame, font=("Arial", 12))
full_name_entry.grid(row=0, column=1, padx=5, pady=5)

username_entry = Entry(frame, font=("Arial", 12))
username_entry.grid(row=1, column=1, padx=5, pady=5)

password_entry = Entry(frame, show="*", font=("Arial", 12))
password_entry.grid(row=2, column=1, padx=5, pady=5)

re_enter_password_entry = Entry(frame, show="*", font=("Arial", 12))
re_enter_password_entry.grid(row=3, column=1, padx=5, pady=5)

phone_number_entry = Entry(frame, font=("Arial", 12))
phone_number_entry.grid(row=4, column=1, padx=5, pady=5)

# Create Gender Radio Buttons
gender_var = StringVar()
gender_var.set("Male")

male_radio = Radiobutton(frame, text="Male", variable=gender_var, value="Male", font=("Arial", 12), fg="#666666", bg="#F0F0F0")
male_radio.grid(row=5, column=1, padx=5, pady=5, sticky="w")

female_radio = Radiobutton(frame, text="Female", variable=gender_var, value="Female", font=("Arial", 12), fg="#666666", bg="#F0F0F0")
female_radio.grid(row=5, column=1, padx=5, pady=5, sticky="e")

# Create Register Button
register_button = Button(root, text="Register", command=register, font=("Arial", 12), fg="#FFFFFF", bg="#337AB7")
register_button.pack(pady=10)

# Create Register Result Label
register_label = Label(root, text="", font=("Arial", 12), fg="green", bg="#F0F0F0")
register_label.pack(pady=5)

# Run the GUI event loop
root.mainloop()
