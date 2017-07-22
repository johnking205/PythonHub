#CryptoPals Challenge #3
#given a hex encoded string, XOR said input against individual characters
#in the alphabet. For each resulting string, grade it based on its containing
#of more common letters
import binascii
import crypto

#input hex value to be XOR'ed by single letter cipher
inputHex = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

#length of the cipher is same as the input (in hex form)
cipherLength = len(inputHex)

#make an array of the bytes for all the letters to be tested as ciphers
alphaByte = [b'41', b'42', b'43', b'44', b'45', b'46', b'47', b'48', b'49', b'4a', b'4b', b'4c', b'4d', b'4e', b'4f', b'50', b'51', b'52', b'53', b'54', b'55', b'56', b'57', b'58', b'59', b'5a', b'61', b'62', b'63', b'64', b'65', b'66', b'67', b'68', b'69', b'6a', b'6b', b'6c', b'6d', b'6e', b'6f', b'70', b'71', b'72', b'73', b'74', b'75', b'76', b'77', b'78', b'79', b'7a']

highScoreHex = ''#to store high score string
highScore = 0#to store high score from letter freq analysis

#For each letter, make a cipher of only that letter and use it as the cipher
for alpha in alphaByte:
    #reinitialize cipher Str for each letter
    cipherStr = b''
    for i in range(cipherLength // 2): #append hex letters to cipher so that
        cipherStr += alpha             #it's the same length as input

    #convert the cipher string to byte form
    #cipherHex is pretty print and can't be used for XORing
    #kept in case of using test print statements below
    cipherHex = binascii.a2b_hex(cipherStr)

    #XOR the cipherStr against the inputHex
    outputHex = crypto.fixedXOR(cipherStr, inputHex)
    #print(outputHex.decode('utf-8'))
    #Score each output for letter frequency
    #try:
    letterCount = crypto.getLetterCount(outputHex.decode('utf-8', errors = 'ignore'))
    #print(outputHex.decode('utf-8', errors = 'ignore'))
    #except:
        #print('no')
        #continue
    outputScore = crypto.letterFreqScore(letterCount)

    #if new high score, save the output
    if outputScore > highScore:
        highScore = outputScore
        highScoreHex = outputHex

print(highScoreHex)
    #compare input str and hex to output str and hex
    #print('str input is  ', cipherHex)
    #print('hex input is  ', cipherStr, '\n')
    #print('str output is ', outputHex)
    #print('hex output is ', binascii.b2a_hex(outputHex))
    #print('\nand if xor +1 ', binascii.b2a_hex(crypto.fixedXOR(cipherStr, binascii.b2a_hex(outputHex))))
    #print('compared 2 og ', inputHex)
