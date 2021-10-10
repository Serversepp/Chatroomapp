import socket
import os

HEADERLEN = 10


def read_conf(file):
    try:
        stat = open(file).readlines()
        ipc = stat[0].split(":")[1]
        portc = stat[1].split(":")[1]

        return str.rstrip(ipc), int(portc)
    except FileNotFoundError:
        f = open(file, "w")
        f.write("IP:127.0.0.1\n")
        f.write("Port:8080")
        f.close()
        if os.name == "posix":  # Used for os detection to get right path
            char = "/"
        else:
            char = "\\"
        raise Exception(f"No config file found \n standard file was created pleas edit under \
        {os.getcwd()} {char} {file}")

    except IndexError:
        raise Exception("WARNING it seems like the config file is bad")


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADERLEN)
        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8"))
        return {"header": message_header, "msg": client_socket.recv(message_length)}
    except:
        return False


HOSTIP, HOSTPORT = read_conf("test.conf")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # using as statement for easy use of socket
    s.bind((HOSTIP, HOSTPORT))  # argument as touple to bind socket
    sockets_list = [s]
    clients = {}  # dict for Clients, socket as key
    s.listen()  # socket server listening for new connections

    conn, addr = s.accept()  # If connection is made, Objekt and address are stored in Variables

    with conn:
        print('Connected with ', addr)
        while True:  # not good
            data = conn.recv(1024)  # recv message from client
            if not data:
                break
            conn.sendall(data)
