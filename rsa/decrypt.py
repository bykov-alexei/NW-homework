import base64

def D(c, d, n):
    return (c ** d) % n

def decrypt(msg, d, n):
    msg = base64.b64decode(msg)
    decrypted = bytearray()
    for i in range(0, len(msg), 4):
        c = int.from_bytes(msg[i:i+4], "little")
        m = D(c, d, n).to_bytes(1, "little")
        decrypted += m
    return decrypted



with open('encrypted.txt', 'rb') as f:
    data = f.read()

with open('private.key', 'r') as f:
    d, n = map(int, f.read().split(" "))


decrypted = decrypt(data, d, n)
with open('decrypted.txt', 'wb') as f:
    f.write(decrypted)
