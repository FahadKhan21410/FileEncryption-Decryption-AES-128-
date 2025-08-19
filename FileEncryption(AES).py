from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad


def EncryptFile(input_file,output_file,key):

    iv = get_random_bytes(16)
    Encryption = AES.new(key,AES.MODE_CBC,iv)
    with open(input_file,'rb') as f:
        plaintext = f.read()

    padPlaintext = pad(plaintext,AES.block_size)
    plaintextEncrypt = Encryption.encrypt(padPlaintext)

    with open(output_file,'wb') as f:
        f.write(iv + plaintextEncrypt) #intialization vector is stored with cipher text for reusing in decryption

    print(f"[Encrypted File] {output_file}")

def DecryptFile(input_file, output_file, key):
    with open(input_file,'rb') as f:
        iv = f.read(16)   # first 16 bytes are the iv we attached at the encryption stage
        ciphertext = f.read()

    Decryption = AES.new(key,AES.MODE_CBC,iv)
    cipherDecrypt = Decryption.decrypt(ciphertext)
    unpaddedPlainText = unpad(cipherDecrypt,AES.block_size)
    with open(output_file,'wb') as f:
        f.write(unpaddedPlainText)

    print(f"[Decrypted File] {output_file}")




key = get_random_bytes(16) #Can vary depending on what algo your are using AES-256 (32 Bytes) but the iv remains same (16 Bytes)
print(f"Key: {key.hex()}") #if you want share your encrypted file with some you can give this to key to them so they can decrypt the file
EncryptFile('C:/Users/TECHNORON/Desktop/Data/password.txt','C:/Users/TECHNORON/Desktop/Encrypted/ciphertext.bin',key)
DecryptFile('C:/Users/TECHNORON/Desktop/Encrypted/ciphertext.bin','C:/Users/TECHNORON/Desktop/Decrypted/plaintext.txt',key)

