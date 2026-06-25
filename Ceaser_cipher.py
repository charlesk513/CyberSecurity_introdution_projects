alphabet = 'abcdefghijklmnopqrstuvwxyz'
user_input = input("word: ")
shift = int(input("Shift: "))
new = ''
for ch in user_input:
    if ch.isalpha():
        index = alphabet.index(ch) + shift
        new_index = (index + shift) % 26
        new += alphabet[new_index]
    else:
        new += ch
print("Cipher text aquired through shifting the index of the character in the original by the shift value forward or backward if negative")
print(f"Cipher text from alphabet: {new}")

#ASCI convention
ascii_ = ""
for i in range(33, 128):
    ascii_+=chr(i)
new = ''
for ch in user_input:
    if ch in ascii_:
        index = ascii_.index(ch) + shift
        new_index = (index + shift) % 94
        new += ascii_[new_index]
    else:
        new += ch
print(f"Cipher text from ASCII: {new}")