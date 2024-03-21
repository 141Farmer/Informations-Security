from pathlib import Path
from math import sqrt
from decimal import getcontext,Decimal

'''def primeValueGenerator(blocks):
    numbers=[0]*100
    for i in range(2,100):
        for j in range(i,100,i):
            numbers[j-1]+=1
    return [i+1 for i in range(100) if numbers[i]==1][:blocks]

def initialHashValueGenerator(primes):
    hashes=[]
    getcontext().prec=40
    for i in primes:    
        sqr=sqrt(i)
        hsqr=sqr.hex()
        hsqr=hsqr[2:][:-2]
        print(hsqr)
        hsqr-=1
        hashes.append(hsqr)
    return hashes
'''


initialHashValues=[
                    0x6a09e667f3bcc908,0xbb67ae8584caa73b,
                    0x3c6ef372fe94f82b,0xa54ff53a5f1d36f1,
                    0x510e527fade682d1,0x9b05688c2b3e6c1f,
                    0x1f83d9abfb41bd6b,0x5be0cd19137e2179
                ]


def paddingBits(string):
    binString=''.join(format(ord(i),'08b') for i in string)
    print(binString)
    lenStr=len(string)*8
    lenShort=64
    lenAppendedBits=-1
    k=1
    while lenAppendedBits<0:
        lenAppendedBits=512*k-lenShort-lenStr
        k+=1
    if lenAppendedBits==0:
        return binString<<lenShort
    else:
        return ((binString<<(lenShort+1))|1)<<(lenAppendedBits-1)
    





def main():
    with open(Path(__file__,'..')/'SHA-512-Input.txt') as file:
        string=file.read()
    blocks=8
    paddedBinStr=paddingBits(string)
    print(paddedBinStr)
    


if __name__=='__main__':
    main()