def encrypt(text,key):
    m,n=len(key),len(text)
    newKey=[]
    ciphertext=''
    for i in range(m,m+n):
        newKey.append(key[i%m])
    j=0
    for i in range(n):
        if not text[i].isalpha():
            ciphertext+=text[i]
            continue
        k=ord(newKey[j])-65 if newKey[j].isupper() else ord(newKey[j])-97
        s=65 if text[i].isupper() else 97
        ciphertext+=chr(((ord(text[i])+k-s)%26)+s)
        j+=1
    return ciphertext

        
def decrypt(text,key):
    m,n=len(key),len(text)
    newKey=[]
    plaintext=''
    for i in range(m,m+n):
        newKey.append(key[i%m])
    j=0
    for i in range(n):
        if not text[i].isalpha():
            plaintext+=text[i]
            continue
        k=ord(newKey[j])-65 if newKey[j].isupper() else ord(newKey[j])-97
        s=65 if text[i].isupper() else 97
        plaintext+=chr(((ord(text[i])-k-s)%26)+s)
        j+=1
    return plaintext
    

def main():
    with open('E:\Fourth Semester\Information Security\VigenreCipherInput.txt','r') as file:
        text=file.readline()
        key=file.readline()
    print(f'Ciphertext: {encrypt(text,key)}')
    print(f'Plaintext: {decrypt(encrypt(text,key),key)}')

if __name__=='__main__':
    main()