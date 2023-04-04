alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input ("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input ("Type your message: \n"). lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_t, shift_position):
  text_to_string = ""
  for letter in plain_t:
    position = alphabet.index(letter)
    new_position = position + shift_position
    new_letter = alphabet[new_position]
    text_to_string += new_letter
  print(f"The encoded text is {text_to_string}")

#TODO-1: Create a different function called "decrypt" that takes the "text" and "shift" as inputs.

#TODO-2: Inside the "decrypt" function, shift each letter of the "text" *backwards* in the alphabet by the shift amount and print the decrypted text. 
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
def decrypt(cipher_t, shift_pos):
  text_to_stringg = ""
  for letter in cipher_t:
    pos = alphabet.index(letter)
    new_pos = pos - shift_pos
    text_to_stringg += alphabet [new_pos]
  print(f"The encoded text is {text_to_stringg}")
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that "direction" variable. You should be able to test the code to encrypt and decrypt a message.
if direction == "encode":
  encrypt(plain_t=text, shift_position=shift)
elif direction == "decode":
  decrypt(cipher_t=text, shift_pos=shift)