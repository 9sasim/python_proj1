from tkinter import *
import socket
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import messagebox
import os
import threading

root = Tk()
root.title("Uniquename")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

# defining select_file function
def select_file():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title='Select Image File',
        filetypes=(('file_type', '*.txt'), ('all files', '*.*'))
    )

def sender():
    def send_file():
        s = socket.socket()
        host = socket.gethostname()
        port = 8989
        s.bind((host, port))
        s.listen(1)
        print(host)
        print('Waiting for connection...')
        conn, addr = s.accept()
        print('Connection established with:', addr)
        file = open(filename, 'rb')
        file_data = file.read(1024)
        total_sent = 0
        while file_data:
            conn.send(file_data)
            total_sent += len(file_data)
            progress = min(total_sent / file_size * 100, 100)
            loading_meter['value'] = progress
            root.update_idletasks()
            file_data = file.read(1024)
        file.close()
        print("Data has been transmitted successfully!!")
        messagebox.showinfo('File Transfer', 'File sent successfully!')

    file_size = os.path.getsize(filename)
    t = threading.Thread(target=send_file)
    t.start()

# defining send function
def send():
    Window = Toplevel(root)
    Window.title("Send")
    Window.geometry('450x560+500+200')
    Window.configure(bg="#f4fdfe")
    Window.resizable(False, False)

    # icon
    icon1 = PhotoImage(file="img/send.png")
    Window.iconphoto(False, icon1)

    Sbg = PhotoImage(file="img/sender.png")
    Label(Window, image=Sbg).place(x=-2, y=0)

    Mbg = PhotoImage(file="img/id.png")
    Label(Window, image=Mbg, bg="#f4fdfe").place(x=100, y=260)

    host = socket.gethostname()
    Label(Window, text=f'ID: {host}', bg='white', fg='black').place(x=140, y=290)

    Button(Window, text="+ Select File", width=10, height=1, font="arial 14 bold", bg="#fff", fg="#000",
           command=select_file).place(x=160, y=150)

    global loading_meter
    loading_meter = Progressbar(Window, orient=HORIZONTAL, length=300, mode='determinate')
    loading_meter.place(x=75, y=220)

    Button(Window, text="Send", width=8, height=1, font="arial 14 bold", fg="#fff", bg="#000", command=sender).place(
        x=300, y=150)

    Window.mainloop()

def receive():
    recc = Toplevel(root)
    recc.title("Receive")
    recc.geometry('450x560+500+200')
    recc.configure(bg="#f4fdfe")
    recc.resizable(False, False)

    def receiver():
        def receive_file():
            ID = SenderID.get()
            filename1 = InFile.get()

            s = socket.socket()
            port = 8989
            s.connect((ID, port))
            file = open(filename1, 'wb')
            file_data = s.recv(1024)
            total_received = 0
            while file_data:
                file.write(file_data)
                total_received += len(file_data)
                progress = min(total_received / file_size * 100, 100)
                loading_meter['value'] = progress
                root.update_idletasks()
                file_data = s.recv(1024)
            file.close()
            print("File received successfully.")
            messagebox.showinfo('File Transfer', 'File received successfully!')

        file_size = os.path.getsize(InFile.get())
        t = threading.Thread(target=receive_file)
        t.start()

    # icon
    icon1 = PhotoImage(file="img/receive.png")
    recc.iconphoto(False, icon1)

    Rbg = PhotoImage(file="img/receiver.png")
    Label(recc, image=Rbg).place(x=-2, y=0)

    logo = PhotoImage(file='img/profile.png')
    Label(recc, image=logo, bg='#f4fdfe').place(x=10, y=250)

    Label(recc, text="Receive", font=('arial', 20), bg="#f4fdfe").place(x=100, y=280)
    Label(recc, text="Input sender ID", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=340)
    SenderID = Entry(recc, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    SenderID.place(x=20, y=370)
    SenderID.focus()

    Label(recc, text="Enter Filename ..", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=420)
    InFile = Entry(recc, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    InFile.place(x=20, y=450)

    global loading_meter
    loading_meter = Progressbar(recc, orient=HORIZONTAL, length=300, mode='determinate')
    loading_meter.place(x=75, y=220)

    imageicon = PhotoImage(file="img/arrow.png")
    rr = Button(recc, text="Receive", compound=LEFT, image=imageicon, width=130, bg="#39c790", font="arial 14 bold",
                command=receiver)
    rr.place(x=20, y=500)

    recc.mainloop()

# icon
image_icon = PhotoImage(file="img/pp.png")
root.iconphoto(False, image_icon)

Label(root, text="File Transfer", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe").place(x=145, y=30)

Frame(root, width=400, height=2, bg="#f3f5f6").place(x=2)

send_img = PhotoImage(file="img/send.png")
send = Button(root, image=send_img, bg="#f4fdfe", bd=0, command=send)
send.place(x=50, y=100)

rec_img = PhotoImage(file="img/receive.png")
rec = Button(root, image=rec_img, bg="#f4fdfe", bd=0, command=receive)
rec.place(x=300, y=100)

# label
Label(root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=300, y=200)

bg = PhotoImage(file="img/background.png")
Label(root, image=bg).place(x=-2, y=323)

root.mainloop()
