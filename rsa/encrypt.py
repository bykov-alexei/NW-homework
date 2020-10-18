import argparse
import base64

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='file')
args = parser.parse_args()

filename = args.file

def E(m, e, n):
    return (m ** e) % n

def encrypt(msg, e, n):
    encrypted = bytearray()
    for i in range(0, len(msg)):
        m = int.from_bytes(msg[i:i+1], "little")
        assert m < n
        c = E(m, e, n)
        b = c.to_bytes(4, "little")
        encrypted += b

    return encrypted

with open(filename, 'rb') as f:
    data = f.read()

with open('public.key', 'r') as f:
    e, n = map(int, f.read().split(" "))

encrypted = encrypt(data, e, n)

with open('encrypted.txt', 'wb') as f:
    f.write(base64.b64encode(encrypted))