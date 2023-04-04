alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(first_text, shift_pos, direction_de):
  last_text = ""
  for letter in first_text:
    pos = alphabet.index(letter)
    if direction_de == "encode":
      new_pos = pos + shift_pos
    elif direction_de == "decode":
      new_pos = pos - shift_pos
    last_text += alphabet[new_pos]
  print(f"The {direction_de}d result is {last_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(first_text=text, shift_pos=shift, direction_de=direction)