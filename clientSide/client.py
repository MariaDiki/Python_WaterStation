import datetime
import socket
from time import sleep
from datetime import date

SERVER_ADDRESS = '192.168.56.1', 5090

keep_running = True
while keep_running:

    fileText = open('status.txt', "r+")
    ID = fileText.readline()
    ALARM1 = fileText.readline()
    ALARM2 = fileText.readline()
    time = datetime.datetime.now()
    dateS = str(date.today())
    timeS = time.strftime("%H:%M")
    data = "{} {} {} {} {}".format(ID, dateS, timeS, ALARM1, ALARM2)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        while True:
            client_socket.sendto(data.encode('utf-8'), SERVER_ADDRESS)
            break
    fileText.close()
    sleep(60)