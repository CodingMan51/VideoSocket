import cv2, pickle, struct, socket

IP = '10.0.0.7'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

data = b''
pacLen = struct.calcsize('Q')

server.bind((IP, PORT))
server.listen(5)

while(True):
    client, addr = server.accept()
    while(client):
        while(len(data) < pacLen):
            packet = client.recv(4096)
            data = data + packet

        pacLenByte = data[:pacLen]
        data = data[pacLen:]

        framePckLen = struct.unpack('Q', pacLenByte)[0]

        while(len(data) < framePckLen):
            packet = client.recv(4096)
            data = data + packet

        framePck = data[:framePckLen]
        data = data[framePckLen:]

        frame = pickle.loads(framePck)

        cv2.imshow('frame', frame)

        key = cv2.waitKey(1) & 0xFF
        if(key == ord('q')):
            break