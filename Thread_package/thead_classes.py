import logging
import socket

from threading import Thread
from time import sleep

from Arduino import arduino_connection
from socket_dir import socket_connection, socket_parser
from gpio_funcs import gpio_func



class ReceiveThread(Thread):
    def __init__(self, host, port):
        super(ReceiveThread,self).__init__()

        self.connection = None
        self.server = socket.socket(
            socket.AF_INET
            , socket.SOCK_STREAM
        )
        self.server.setsockopt(
            socket.SOL_SOCKET
            , socket.SO_REUSEADDR
            , 1
        )
        self.server.bind(('',4662))
        self.server.listen(1)

    def run(self):
        logging.info("ReceiveThread Thread - Starting ")
        #socket_connection.socker_bind_connection()
        while 1:
            #connection can terminate at anytime
            #Try catch??
            connection, addr = self.server.accept()
            rcvd_data = connection.recv(4096).decode("utf-8")
            if rcvd_data:
                socket_parser.rasp_parser(rcvd_data)


class SendThread(Thread):
    def __init__(self):
        super(SendThread,self).__init__()

    def run(self):
        pass
        logging.info("Thread Function - Starting " + self.name)
        socket_connection.send_socket()
        #logging.info("Thread Function - Exiting " + self.name)


class PortoDoorThread(Thread):
    def __init__(self):
        super(PortoDoorThread,self).__init__()

    def run(self):
        pass
        logging.info("Porto_Door_thead - Starting")
        gpio_func.Porto_door_checker()
        logging.info("Porto_Door_thead -Exiting ")