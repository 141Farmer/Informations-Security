from math import sqrt
from random import randbytes

blockSize=16
rounds=10

sbox=[
        0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
        0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
        0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
        0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
        0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
        0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
        0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
        0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
        0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
        0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
        0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
        0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
        0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
        0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
        0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
        0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16
    ]

inverse_sbox = [
    0x52,0x09,0x6a,0xd5,0x30,0x36,0xa5,0x38,0xbf,0x40,0xa3,0x9e,0x81,0xf3,0xd7,0xfb,
    0x7c,0xe3,0x39,0x82,0x9b,0x2f,0xff,0x87,0x34,0x8e,0x43,0x44,0xc4,0xde,0xe9,0xcb,
    0x54,0x7b,0x94,0x32,0xa6,0xc2,0x23,0x3d,0xee,0x4c,0x95,0x0b,0x42,0xfa,0xc3,0x4e,
    0x08,0x2e,0xa1,0x66,0x28,0xd9,0x24,0xb2,0x76,0x5b,0xa2,0x49,0x6d,0x8b,0xd1,0x25,
    0x72,0xf8,0xf6,0x64,0x86,0x68,0x98,0x16,0xd4,0xa4,0x5c,0xcc,0x5d,0x65,0xb6,0x92,
    0x6c,0x70,0x48,0x50,0xfd,0xed,0xb9,0xda,0x5e,0x15,0x46,0x57,0xa7,0x8d,0x9d,0x84,
    0x90,0xd8,0xab,0x00,0x8c,0xbc,0xd3,0x0a,0xf7,0xe4,0x58,0x05,0xb8,0xb3,0x45,0x06,
    0xd0,0x2c,0x1e,0x8f,0xca,0x3f,0x0f,0x02,0xc1,0xaf,0xbd,0x03,0x01,0x13,0x8a,0x6b,
    0x3a,0x91,0x11,0x41,0x4f,0x67,0xdc,0xea,0x97,0xf2,0xcf,0xce,0xf0,0xb4,0xe6,0x73,
    0x96,0xac,0x74,0x22,0xe7,0xad,0x35,0x85,0xe2,0xf9,0x37,0xe8,0x1c,0x75,0xdf,0x6e,
    0x47,0xf1,0x1a,0x71,0x1d,0x29,0xc5,0x89,0x6f,0xb7,0x62,0x0e,0xaa,0x18,0xbe,0x1b,
    0xfc,0x56,0x3e,0x4b,0xc6,0xd2,0x79,0x20,0x9a,0xdb,0xc0,0xfe,0x78,0xcd,0x5a,0xf4,
    0x1f,0xdd,0xa8,0x33,0x88,0x07,0xc7,0x31,0xb1,0x12,0x10,0x59,0x27,0x80,0xec,0x5f,
    0x60,0x51,0x7f,0xa9,0x19,0xb5,0x4a,0x0d,0x2d,0xe5,0x7a,0x9f,0x93,0xc9,0x9c,0xef,
    0xa0,0xe0,0x3b,0x4d,0xae,0x2a,0xf5,0xb0,0xc8,0xeb,0xbb,0x3c,0x83,0x53,0x99,0x61,
    0x17,0x2b,0x04,0x7e,0xba,0x77,0xd6,0x26,0xe1,0x69,0x14,0x63,0x55,0x21,0x0c,0x7d
]

roundConstants=[0x8d,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1b,0x36]

def padding(data,blockSize):
    padSize=blockSize-len(data)
    padding=([padSize])*padSize
    return data+padding

def removePadding(data):
    paddingLength=data[-1]
    unpaddedData=data[:-paddingLength] 
    return unpaddedData


def Generate(block_size):
    return randbytes(block_size)

def g(word,roundConstant):
    rotatedWord=word[1:]+word[:1]
    substitutedWord=[sbox[c] for c in rotatedWord]
    substitutedWord[0]^=roundConstant
    return substitutedWord

def expandedKeysGenerate(masterKey):
    expandedKeys=[]
    numWords=44
    words=[None]*numWords
    for i in range(4):
        temp=[]
        for j in range(4):
            temp.append(masterKey[4*i+j])
        words[i]=temp
    for i in range(4,numWords):
        temp=[]
        if i%4==0:
            for j in range(4):
                temp.append(g(words[i-1],i//4)[j]^words[i-4][j])
        else:
            for j in range(4):
                temp.append(words[i-4][j]^words[i-1][j])
        words[i]=temp
    for i in range(0,numWords,4):
        temp=[]
        for j in range(i,i+4):
            for k in range(4):
                temp.append(words[j][k])
        expandedKeys.append(temp)
    return expandedKeys

def ByteSub(state):
    it=len(state)
    for i in range(it):
        state[i]=sbox[state[i]]
    return state

def InverseByteSub(state):
    it=len(state)
    for i in range(it):
        state[i]=inverse_sbox[state[i]]
    return state

def ShiftRow(state):
    it=int(sqrt(len(state)))
    for i in range(1,it):
        stind=i*4
        endind=stind+i
        state[stind:stind+it]=state[endind:stind+it]+state[stind:endind]
    return state

def InverseShiftRow(state):
    it=int(sqrt(len(state)))
    for i in range(1,it):
        stind=i*4
        endind=stind+it-i
        state[stind:stind+it]=state[endind:stind+it]+state[stind:endind]
    return state

def galMul(x,y):
    product=0
    for _ in range(8):
        if y&1==1:
            product^=x
        highBitSet=x & 0x80
        x<<=1
        if highBitSet==0x80:
            x^=0x1b
        y>>=1
    return product & 0xff

def MixColumn(state):
    it=int(sqrt(len(state)))
    resultMatrix=[None]*(it*it)
    for i in range(it):
        resultMatrix[4*i+0]=galMul(state[4*i+0],2)^state[4*i+3]^state[4*i+2]^galMul(state[4*i+1],3)
        resultMatrix[4*i+1]=galMul(state[4*i+1],2)^state[4*i+0]^state[4*i+3]^galMul(state[4*i+2],3)
        resultMatrix[4*i+2]=galMul(state[4*i+2],2)^state[4*i+1]^state[4*i+0]^galMul(state[4*i+3],3)
        resultMatrix[4*i+3]=galMul(state[4*i+3],2)^state[4*i+2]^state[4*i+1]^galMul(state[4*i+0],3)
    return resultMatrix

def InverseMixColumn(state):
    it=int(sqrt(len(state)))
    resultMatrix=[None]*(it*it)
    for i in range(it):
        resultMatrix[4*i+0]=galMul(state[4*i+0],14)^galMul(state[4*i+3],9)^galMul(state[4*i+2],13)^galMul(state[4*i+1],11)
        resultMatrix[4*i+1]=galMul(state[4*i+1],14)^galMul(state[4*i+0],9)^galMul(state[4*i+3],13)^galMul(state[4*i+2],11)
        resultMatrix[4*i+2]=galMul(state[4*i+2],14)^galMul(state[4*i+1],9)^galMul(state[4*i+0],13)^galMul(state[4*i+3],11)
        resultMatrix[4*i+3]=galMul(state[4*i+3],14)^galMul(state[4*i+2],9)^galMul(state[4*i+1],13)^galMul(state[4*i+0],11)
    return resultMatrix

def XOR(State,keyMatrix):
    result=[]
    it=len(State)
    for i in range(it):
        result.append(State[i]^keyMatrix[i])
    return result

def aesBlockEncrypt(plaintext,keys):
    ciphertext=plaintext

    ciphertext=XOR(ciphertext,keys[0]) 

    for i in range(1,rounds):
        ciphertext=ByteSub(ciphertext)
        ciphertext=ShiftRow(ciphertext)
        ciphertext=MixColumn(ciphertext)
        ciphertext=XOR(ciphertext,keys[i])

    ciphertext=ByteSub(ciphertext)
    ciphertext=ShiftRow(ciphertext)
    ciphertext=XOR(ciphertext,keys[-1])

    return ciphertext

def aesBlockDecrypt(ciphertext,keys):
    plaintext=XOR(ciphertext,keys[-1]) 

    for i in range(rounds-1,0,-1):
        plaintext=InverseShiftRow(plaintext)
        plaintext=InverseByteSub(plaintext)
        plaintext=XOR(plaintext,keys[i])
        plaintext=InverseMixColumn(plaintext)
        
    plaintext=InverseShiftRow(plaintext)
    plaintext=InverseByteSub(plaintext)
    plaintext=XOR(plaintext,keys[0])

    return plaintext

def aesEncrypt(plaintext,keys,iV):
    length=len(plaintext)

    ciphertext=[]
    plaintext=[ord(c) for c in plaintext]

    currentVector=iV

    for i in range(0,length,blockSize):
        string=plaintext[i:i+blockSize]
        string=padding(string,blockSize)
        plaintemptext=XOR(string,currentVector)
        ciphertemptext=aesBlockEncrypt(plaintemptext,keys)
        currentVector=ciphertemptext
        ciphertext+=ciphertemptext

    return ciphertext

def aesDecrypt(ciphertext,keys,iV):
    length=len(ciphertext)

    plaintext=[]
    ciphertext=[ord(c) for c in ciphertext]
    
    currentVector=iV

    for i in range(0,length,blockSize):
        string=ciphertext[i:i+blockSize]
        ciphertemptext=aesBlockDecrypt(string,keys)
        plaintemptext=XOR(ciphertemptext,currentVector)
        currentVector=string
        plaintext+=plaintemptext

    return plaintext

def main():

    with open("AES-Input.txt","r") as file:
        plaintext=file.read()   
    print("Plain data     : ",plaintext)

    initialVector=Generate(blockSize)
    print('Initial vector : ',initialVector)

    masterKey=Generate(blockSize)
    keys=expandedKeysGenerate(masterKey)
    print('Master Key     : ',masterKey)
    
    encryptedtext=aesEncrypt(plaintext,keys,initialVector)
    encryptedtext=''.join(chr(c) for c in encryptedtext)
    print('Encrypted text : ',encryptedtext)

    decryptedtext=aesDecrypt(encryptedtext,keys,initialVector)
    decryptedtext=removePadding(decryptedtext)
    decryptedtext=''.join(chr(c) for c in decryptedtext)
    print('Decrypted text : ',decryptedtext)
    
if __name__=='__main__':
    main()