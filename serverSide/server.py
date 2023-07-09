import socket
import sqlite3

SERVER_ADDRESS = '192.168.56.1', 5090

#                       IP + port         UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_sock:
    server_sock.bind(SERVER_ADDRESS)

    while True:
        data, sender_addr = server_sock.recvfrom(1024)
        message = data.decode('utf-8')
        print('{} --> {}'.format(sender_addr, message))
        info = message.split()
        stationId = info[0]
        lastDate = info[1] + " " + info[2]
        a1 = info[3]
        a2 = info[4]

        con = sqlite3.connect('data.sqlite')
        with con:
            cur = con.cursor()
            q = """
            INSERT or REPLACE into Station_Status
            values (?, ?, ?, ?)
            """
            updateVal = (stationId, lastDate, a1, a2)
            cur.execute(q, updateVal)
            con.commit()
        con.close()
