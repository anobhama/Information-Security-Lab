# Vigenere Cipher 

def generateKey(string, keyword): 
	key = list(keyword) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) - len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key)) 
	
def cipherText(string, keyword): 
	cipher_text = [] 
	for i in range(len(string)): 
		x = (ord(string[i]) + ord(key[i])) % 26
		x += ord('A') 
		cipher_text.append(chr(x)) 
	return("" . join(cipher_text)) 
	
def originalText(cipher_text, keyword): 
	orig_text = [] 
	for i in range(len(cipher_text)): 
		x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
		x += ord('A') 
		orig_text.append(chr(x)) 
	return("" . join(orig_text)) 

string = input("Enter the text: ")
keyword = input("Enter the keywrd: ")
key = generateKey(string, keyword) 
cipher_text = cipherText(string,key) 
print("Ciphertext :", cipher_text) 
print("Decrypted Text :", originalText(cipher_text, key)) 