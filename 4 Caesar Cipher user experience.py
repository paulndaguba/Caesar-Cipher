alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
def caesar(first_text, shift_pos, direction_de):
  last_text = ""
  if direction_de == "decode":
    shift_pos *= -1
  for char in first_text:
    if char in alphabet:
      pos = alphabet.index(char)
      new_pos = pos + shift_pos
      last_text += alphabet[new_pos]
    else:
      last_text += char
    
  print(f"Here's the {direction_de}d result: {last_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
prog_continue = True
while prog_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #TODO-2: What if the user enters a shift that is
  #greater than the number of letters in the alphabet?
  #Try running the program and entering a shift
  #number of 45.
  #Add some code so that the program continues to
  #work even if the user enters a shift number
  #greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(first_text=text, shift_pos=shift, direction_de=direction)

  user_answer = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
  if user_answer == "no":
    prog_continue = False
    print("Goodbye")