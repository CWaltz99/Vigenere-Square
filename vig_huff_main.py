from huffman import Huffman
from vigenere import Vigenere
import codecs
       
def main():
    """
    DO NOT change this file
    """
    INPUT_FILE = "FDREconomics.txt"    
    DECRYPT_FILE = "FDREconomicsDecrypt.txt"
    ENCRYPT_FILE = "FDREconomicsEncrypt.txt"        
    DECRYPT_COMPRESS_FILE = "FDREconomicsDecryptComp.txt"
    
    VIGENERE_KEY = "Give PEACE a chance!!"
    
    print("(1) Read in original file from " + INPUT_FILE)
    print("    Print the original file:")
    print()

    file_str = open(INPUT_FILE, 'r').read()
    print(file_str)
    print() 
    
    print("(2) Encrypt original file using key: " + VIGENERE_KEY)
    print()

    vig = Vigenere(VIGENERE_KEY)
    en_file_str = vig.encrypt(file_str)

    print("(3) Write out the encrypted file to " + ENCRYPT_FILE)
    print()
    
    codecs.open(ENCRYPT_FILE, 'w', encoding='utf8').write(en_file_str)

    print("(4) Read in encrypted original file from " + ENCRYPT_FILE)
    print("    Decrypt encrypted file using key")
    print("    Print out decrypted file:")
    print()

    en_file_str = codecs.open(ENCRYPT_FILE, 'r', encoding='utf8').read()
    message = vig.decrypt(en_file_str)
    print(message)
    print()

    print("(5) Write out the decrypted file to " + DECRYPT_FILE)
    print()

    open(DECRYPT_FILE, 'w').write(message)

    
    print("(6) Compress the original file and save in string")
    print()

    huff = Huffman()
    binary_str = huff.compress(file_str)

    print("(7) Decompress compressed file from the string")
    print("    Print out decompressed file")
    print()
        
    message = huff.decompress(binary_str)
    print(message)
    print()

    print("(8) Encrypt original file using key")
    print()

    vig = Vigenere(VIGENERE_KEY)
    en_file_str = vig.encrypt(file_str)
    
    print("(9) Compress the encrypted file and save in string")
    print()

    huff = Huffman()
    binary_str = huff.compress(en_file_str)

    print("(10) Decompress compressed encrypted file from the string")
    print()
 
    message = huff.decompress(binary_str)

    print("(11) Decrypt decompressed encrypted file using key")
    print("     Print out decrypted decompressed encrypted file")
    print()

    file_str = vig.decrypt(message)
    print(file_str)
    print()
    
    print("(12) Write out the decrypted decompressed file to " + DECRYPT_COMPRESS_FILE)
    
    open(DECRYPT_COMPRESS_FILE, 'w').write(file_str)
    
main()
