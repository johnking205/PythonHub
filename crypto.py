import binascii

#Hex string to base64 string Cryptopals Challenge #1)
#Input: string representing hex value
#Output: base64 conversion of input in byte format
def hex2Base64(hexValue):
    # decode hex input string to binary
    binaryOutput = binascii.a2b_hex(hexValue)

    # convert bytes to base64
    #b2a_base64 outputs with newline character at end.
    #[:-1] slices that newline off the end
    return binascii.b2a_base64(binaryOutput)[:-1]

#Fixed XOR Function (CryptoPals Challenge #2)
#Input: Two equal length hex strings
#Output: The XOR Combination of the two inputs in byte format
def fixedXOR(hexString1, hexString2):
    #Convert hex string inputs into binary
    binaryBuff1 = binascii.a2b_hex(hexString1)
    binaryBuff2 = binascii.a2b_hex(hexString2)

    #convert bytes into int
    intBuff1 = int.from_bytes(binaryBuff1, byteorder='big')
    intBuff2 = int.from_bytes(binaryBuff2, byteorder='big')
    
    #check if buffers are same length and return 0 so error handler can work
    #if len(hex(intBuff1 ^ intBuff2)[2:]) % 2:
    #    return 0
    #XOR the ints together and return hex converted result
    #note: the output of hex() is a string with '0x' at the front.
    #[2:] 'slices' that '0x' off the front of the string so that
    #a2b_hex can convert it to binary w/o freaking about the 0x
    try:
    #print(hex(intBuff1 ^ intBuff2)[2:])
        return binascii.a2b_hex(hex(intBuff1 ^ intBuff2)[2:])
    except:
        return binascii.a2b_hex('0' + hex(intBuff1 ^ intBuff2)[2:])
#Alternative to fixedXOR
def xor(b1, b2):
    b = bytearray(len(b1))
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b

#Count how many times a letter (not case sensitive) shows up in messsage
#Taken from https://inventwithpython.com/freqAnalysis.py
#Input: string message
#Output: dictionary with how much each letter was in message
def getLetterCount(message):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    # non-letters (denoted !) are counted as well so they can be penalized later
    # common non-letters (' ' and ',') counted so as not to be penalized
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, ' ': 0, "'": 0, '!': 0}
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
    
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
        else:
            letterCount['!'] += 1

    return letterCount

#Given a dictionary containing the frequency of each letter
#(see getLetterCount for desired format), score the frequency of the string that
#produced the letterCount string
#Input: letterCount Dictionary
#Output: number score
def letterFreqScore(letterCount):
    #percent value for letters in alphabetic order
    #at end is negative score for non-letters
    englishLetterFreq = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4, 6.7, 7.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1, -10.0, 0, 0]
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ! '"
    index = 0 #index for going through LETTERS
    scoreTotal = 0
    for letter in englishLetterFreq:
        scorePerLetter = letter * letterCount[LETTERS[index]]
        index += 1
        scoreTotal += scorePerLetter
    return scoreTotal

#alphaByteCipher
#given a hex encoded string, XOR said input against individual characters
#in the alphabet. For each resulting string, grade it based on its containing
#of more common letters
def alphaByteCipher(inputHex):
    #input hex value to be XOR'ed by single letter cipher
    #inputHex = b'1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

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
        #check for several errors and skip to next iteration if error
        #if len(cipherStr) != len(inputHex):
        #    continue
        #outputHex = fixedXOR(cipherStr, inputHex)
        #print(bytearray(cipherStr).decode())
        outputHex = str(xor(bytearray(cipherStr), bytearray(inputHex)))
        #if outputHex == 0:
        #    continue
        #Score each output for letter frequency
        #print(outputHex)
        letterCount = getLetterCount(outputHex)
        outputScore = letterFreqScore(letterCount)

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
    return highScoreHex
