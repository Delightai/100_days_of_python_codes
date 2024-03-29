alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")



plain = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    encrypt_text = ""
    for letters in plain_text:
        position = alphabet.index(letters)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        encrypt_text += new_letter 

    print (f"Your encrpted text is {encrypt_text}")

def decrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    cipher_text += alphabet[new_position]
  print(f"The decoded text is {cipher_text}")

if direction == "encode":
   encrypt(plain_text=plain, shift_amount=shift) 
else:
   decrypt(plain_text=plain, shift_amount=shift)

