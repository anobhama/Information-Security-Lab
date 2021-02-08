def encrypt(text,s): 
	result = "" 
	for i in range(len(text)): 
		char = text[i]
		if (char.isupper()): 
			result += chr((ord(char) + s - 65) % 26 + 65) 
		else: 
			result += chr((ord(char) + s - 97) % 26 + 97) 
	return result 

def decrypt(s, text):
    text = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in text:
        if letter in alpha:
            letter_index = (alpha.find(letter) - s) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    print("decrypted text is ",result.lower())
text = input("enter the text: ")
s = int(input("Enter the key: "))
print ("Cipher: " + encrypt(text,s))
decrypt(s,text)	