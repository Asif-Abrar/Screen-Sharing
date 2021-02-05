from vidstream import StreamingServer
import threading

receiver = StreamingServer('192.168.0.105', 9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input('') != 'stop':
    continue

receiver.stop_server()
