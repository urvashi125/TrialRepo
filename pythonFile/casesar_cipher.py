alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#list_text = text.
#print(list_text)
def function_to_encrypt_dcrypt(direction,text,shift):
    cipher_text = ""
    if(direction == "encode"):
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"encoded message is {cipher_text}")
    if(direction == "decode"):
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"decoded message is {cipher_text}")

function_to_encrypt_dcrypt(direction=direction,text=text,shift=shift)