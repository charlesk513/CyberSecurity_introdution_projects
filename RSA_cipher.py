
e, n = 17, 1271
mapping = ""
for i in range(34, 128):
    mapping+=chr(i)
text = input("Enter the text to encrypt: ").lower()
cipher_texts = [pow(mapping.index(ch), e, n) for ch in text]
print("Below are the cypher numerals of the text entered")
print(','.join(str(c) for c in cipher_texts))
