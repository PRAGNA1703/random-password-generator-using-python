import random
import string

def generate_password(min_length, numbers = True, special_characters = True ):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    if numbers:  
        characters += digits 
    if special_characters:
         characters += special 
    
    pwd = ""
    meets_condition = False
    has_number = False
    has_special = False
  
     
    while not meets_condition or len(pwd) < min_length:
         new_char = random.choice(characters)
         pwd += new_char
    if new_char in digits:
         has_number = True
    elif new_char in special :
         has_special = True
         
         meets_condition = True 
         
    if numbers:
            meets_condition = has_number
    if special_characters:
            meets_condition =  meets_condition and has_special
   
    
    return pwd

min_length = int(input("Enter the min length: "))
has_number = input("Do you want numbers:(y/n)? ").lower() == "y"
has_special = input("Do you want special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special) 
print("The generated password is:",pwd) 
 

