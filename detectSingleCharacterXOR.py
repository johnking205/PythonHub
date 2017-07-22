#Cryptopals Set 1 Challenge 4
#given a .txt file with hex encoded strings seperated by newlines
#detect which string was encrypted by single character XOR
import crypto
#parse input text file into b'blah' format strings
f = open('C:\\Users\\John\\Documents\\VSCode\\Crypto4.txt', 'r')
for i in range(60):
    inputStr = f.readline()[:-1]
    inputHex = inputStr.encode("utf-8", 'replace')
    ###need to determine if all bytes are valid utf-8
    crypto.alphaByteCipher(inputHex)
    #print(inputStr)
f.close()