from hashlib import sha512
from pathlib import Path
with open(Path(__file__,'..')/'SHA-512-Input.txt') as file:
    string=file.read()
string=''
s512=(sha512(string.encode())).hexdigest()

print(s512)
print(type(s512),len(s512))