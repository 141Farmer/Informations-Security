from hashlib import sha512
from pathlib import Path
with open(Path(__file__,'..')/'SHA-512-Input.txt') as file:
    string=file.read()

print((sha512(string.encode())).hexdigest())