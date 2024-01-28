def encrypt(text,key):
    ciphertext=''
    for c in text:
        if c.isalpha():
            s=ord('A') if c.isupper() else ord('a')
            c=chr(((ord(c)-s+key)%26)+s)
        ciphertext+=c
    return ciphertext
        
def decrypt(text,key):
    plaintext=''
    for c in text:
        if c.isalpha():
            s=ord('A') if c.isupper() else ord('a')
            c=chr(((ord(c)-s-key)%26)+s)
        plaintext+=c
    return plaintext

def main():
    with open('E:\Fourth Semester\Information Security\CaesarCipherInput.txt','r') as file:
        text=file.readline()
        key=int(file.readline())
    print(f'Ciphertext: {encrypt(text,key)}')
    print(f'Plaintext: {decrypt(encrypt(text,key),key)}')

if __name__=='__main__':
    main()