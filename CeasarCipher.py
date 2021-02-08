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

    for i in text:
        if i in alpha:
            i_index = (alpha.find(i) - s) % 26

            result = result + alpha[i_index]
        else:
            result = result + i

    print("decrypted text is ",result.lower())
text = input("enter the text: ")
s = int(input("Enter the key: "))
print ("Cipher: " + encrypt(text,s))
decrypt(s,text)	