import os
import socket
import sys


try:
    host = input("give ip or domain name: ")
    ip = socket.gethostbyname(host)
    print("host: " + host)
    print("website ip: " + ip)
except:
    print("error, check your internet connection and try again")

