import socket
import sys
import os

filepath = sys.argv[1]
HOST = sys.argv[2]
PORT = int(sys.argv[3])
CHUNK_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    filename = filepath.split('/')[-1]
    f = open(filepath, 'rb')
    filesize = os.stat(filepath).st_size
    print(filesize)
    l = f.read(CHUNK_SIZE)
    s.connect((HOST, PORT))
    s.send(bytes(filename, 'utf-8'))
    resp = s.recv(CHUNK_SIZE)
    if resp == b'ok':
        i = 1
        while l:
            s.send(l)
            if i*CHUNK_SIZE >= filesize:
                print(f"Transfer Progress: 100%")
            else:
                print(f"Transfer Progress: {100 * (i * CHUNK_SIZE / filesize)}%", flush=True)
            i += 1
            l = f.read(CHUNK_SIZE)