import cv2, struct, socket, pickle

IP = '10.0.0.7'
PORT = 9999

vid = cv2.VideoCapture(0)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((IP, PORT))
print(f'Connected Successfully To: {IP}:{PORT}')

while(True):
    while(vid.isOpened()):
        suc, frame = vid.read()
        framePck = pickle.dumps(frame)
        framePckSize = struct.pack('Q', len(framePck))
        packet = framePckSize + framePck
        server.sendall(packet)