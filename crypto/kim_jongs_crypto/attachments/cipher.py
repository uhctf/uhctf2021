# Our supreme leader's state-of-the-art encryption algorithm.
# Developed by: Kim Jong Un
# Developed for: Kim Jong Un
# Note: plaintext is ONLY alphanumeric (capital and non-capital)

import sys

# Input plain text
plainText = sys.argv[1]

# Output ciphertext
cipherText = ""


cipherText += str(ord(plainText[0]) & 0xDEAF) + "-"
for i, char in enumerate(plainText[1:]):
    cipherText += str((ord(char) & 0xAAAA)-ord(plainText[i])) + "-" + str(ord(char) & (0x7518 ^ ord(plainText[0]))) + "-"


print("Ciphertext: " + cipherText)
