from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def DecryptFile(input_file,output_file,key):
    try:
        with open(input_file,'rb') as f:
            iv = f.read(16)
            ciphertext = f.read()

        Decryption = AES.new(key,AES.MODE_CBC,iv)
        cipherDecrypt = Decryption.decrypt(ciphertext)
        unpaddedCipher = unpad(cipherDecrypt,AES.block_size)

        with open(output_file,'wb') as f:
            f.write(unpaddedCipher)

    except ValueError as e:
        print("Decryption failed (possible wrong key or corrupted file):", e)

    except FileNotFoundError:

        print("File not found. Please check the input path.")

    except Exception as e:
        print("An error occurred:", e)


print("===AES128 DECRYPTION TOOL===")
key = bytes.fromhex(input("[Please Enter Your 32-Character Hex Key] "))
if len(key) != 16: # 1 byte = 2 hex characters so,32 hex character / 2 = 16 Bytes
    print("Invalid key length. Must be 32 hex characters (16 bytes for AES-128).")
    exit(1)

input_path = input("Enter path to encrypted file (.bin):\n> ")
output_path = input("Enter path to save decrypted file (.txt):\n> ")

DecryptFile(input_path,output_path,key)
print("File Decrypted Successfully")

