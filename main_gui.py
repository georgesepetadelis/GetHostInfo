import socket
from tkinter import *

root = Tk()
root.geometry("350x350")
root.title("Get Host Info")
root.configure(bg="blue")


def result():
    try:
        host = host_in.get()
        ip = socket.gethostbyname(host)
        ip_res = "Host ip: " + ip
        display_ip = Label(root, text=ip_res, bg="blue", fg="white")
        display_ip.pack()
    except:
        error = Label(root, text="error, please check your connection or domain name", fg="red",bg="blue")
        error.pack()

Label(root, text="Type domain name\n", bg="blue").pack()
host_in = Entry(root)
host_in.pack()
Label(root, text="", bg="blue").pack()
submit = Button(root, text="Get Host Info", command=result)
submit.pack()
root.mainloop()




