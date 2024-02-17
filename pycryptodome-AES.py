from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from pathlib import Path

def encrypt(plaintext,key):
    cipher=AES.new(key,AES.MODE_ECB)
    ciphertext=cipher.encrypt(pad(plaintext,AES.block_size))

    return ciphertext


def decrypt(ciphertext,key):
    plain=AES.new(key,AES.MODE_ECB)
    plaintext=unpad(plain.decrypt(ciphertext),AES.block_size)
    return plaintext


def main():

    with open(Path(__file__,'..')/'AES-Input.txt','r') as file:
        plaintext=file.readline()
    plainbytes=bytes(plaintext,'utf-8')
    print('Plaintext : ',plaintext)

    key=get_random_bytes(16)
    print('Key : ',key)

    cipherbytes=encrypt(plainbytes,key)
    ciphertext=''.join(map(chr,cipherbytes))
    print('Ciphertext : ',ciphertext)

    decryptedbytes=decrypt(cipherbytes,key)
    decryptedtext=''.join(map(chr,decryptedbytes))
    print('Decryptedtext : ',decryptedtext)


if __name__=='__main__':
    main()