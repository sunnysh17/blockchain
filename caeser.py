def encrypt(text,s):
    
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(ciphertext, s):
    result = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result

#check the above function
text = input("Enter Plain Text: ")
s = int(input("Enter shift key: "))
print("==========================================")
print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Cipher Text: " + encrypt(text,s))

print("==========================================")
# Check the decryption function
ciphertext = encrypt(text, s)  # Encrypt the text using the provided encryption function
print("Cipher Text : " + ciphertext)
print("Shift pattern : " + str(s))
print("Decrypted Text: " + decrypt(ciphertext, s))