from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root=Tk()
root.title("Uniquename")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(True,True)

#icon 
image_icon=PhotoImage(file="img/pp.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)

Frame(root,width=400,height=2,bg="#f3f5f6").place(x=2)

send_img=PhotoImage(file="img/ss.png")
send=Button(root,image=send_img,bg="#f4fdfe",bd=0)
send.place(x=300,y=100)

#label
Label(root, text="Send", font=('Acumin Variable Concept', 17, 'bold'),bg="#f4fdfe").place(x=65,y=200)
Label (root, text="Receive", font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=300,y=200)



rec_img=PhotoImage(file="img/ss.png")
rec=Button(root,image=rec_img,bg="#f4fdfe",bd=0)
rec.place(x=50,y=100)



root.mainloop()