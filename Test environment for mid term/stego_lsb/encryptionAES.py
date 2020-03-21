
 
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import sys
 
from hashlib import md5			#encripting AES KEY
from base64 import b64decode    
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_ECB) #uses code block cipher varient with initial vector iv
        return b64encode(self.cipher.encrypt(pad(data.encode('utf-8'), 
            AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_ECB, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)


if __name__ == '__main__':
    print('ENCRYPTION')
    pwd = input('Password..: ')
    with open(sys.argv[1], 'r') as i:
        with open(sys.argv[2],'w') as o:
            for line in i:
                o.write(AESCipher(pwd).encrypt(line).decode('utf-8'))
    i.close()
    o.close()

    
    print('Decryption')
    pwd2 = input('password--- ')
    if(pwd==pwd2):
        with open(sys.argv[2],'r') as id:
            for li in id:
                cont = id.readline().split('==')
                for j in cont:
                    print(AESCipher(pwd).decrypt(j).decode('utf-8'))

    

    