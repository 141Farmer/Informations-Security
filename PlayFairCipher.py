def generateKey(key):
    keyArray=['' for _ in range(25)] 
    keyMatrix=[['' for _ in range(5)] for _ in range(5)]
    alpha=[chr(i) for i in range(65,65+26)]
    j,k,l=0,0,len(key)

    for i in range(25):
        if k<l:
            while k<l:
                if key[k] not in keyArray:
                    keyArray[i]=key[k]
                    k+=1
                    break
                k+=1
        else:
            while True:
                if alpha[j] not in keyArray:
                    keyArray[i]=alpha[j]
                    j+=1
                    break
                j+=1
    for i in range(5):
        for j in range(5):
            keyMatrix[i][j]=keyArray[i*5+j]

    return keyMatrix


def partText(text):
    l=len(text)
    part=['' for _ in range(l//2)]
    for i in range(0,l-2,2):
        if text[i]!=text[i+1]:
            part[i//2]=text[i]+text[i+1]
        else:
            next=chr((ord(text[i])+1))
            prev=chr((ord(text[i])-1))
            if next.isalpha():
                part[i//2]=text[i]+next
            else:
                part[i//2]=text[i]+prev
    return part

def crypt(text,keyMatrix):
    part=partText(text)
    print(part)
    ciphertext=''
    for chars in part:
        if len(chars)!=2:
            break
        ax,ay,bx,by=-1,-1,-1,-1
        for i in range(5):
            for j in range(5):
                if keyMatrix[i][j]==chars[0]:
                    ax,ay=i,j
                elif keyMatrix[i][j]==chars[1]:
                    bx,by=i,j
        if ay==by:
            ciphertext+=(keyMatrix[(ax+1)%5][ay]+keyMatrix[(bx+1)%5][by])
        elif ax==bx:
            ciphertext+=(keyMatrix[ax][(ay+1)%5]+keyMatrix[bx][(by+1)%5])
        else:
            ciphertext+=(keyMatrix[ax][by]+keyMatrix[bx][ay])
    
    return ciphertext


def main():
    with open('E:\Fourth Semester\Information Security\PlayFairCipherInput.txt','r') as file:
        text=file.readline()
        key=file.readline()
    keyMatrix=generateKey(key)
    print(keyMatrix)
    ciphertext=crypt(text,keyMatrix)
    print(f'Ciphertext: {ciphertext}')
    Plaintext=crypt(ciphertext,keyMatrix)
    print(f'Plaintext: {Plaintext}')

if __name__=='__main__':
    main()