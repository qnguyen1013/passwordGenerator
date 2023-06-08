import random
import string

#function for generating password where we can specify minimum length and whether or not it contains special chars or nums
def generate_password(min_length, numbers=True, special_characters=True):
    if min_length <= 0 or min_length >= 100:
        raise Exception("Sorry, please enter a valid minimum length between 1 and 100")

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    choiceSet = letters
    if numbers:
        choiceSet += digits
    if special_characters:
        choiceSet += special_chars
    
    password = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        #picks random element from the string 
        new_char = random.choice(choiceSet)
        password += new_char

        if new_char in digits:
            has_number = True
        if new_char in special_chars:
            has_special = True
        
        #convention is to set criteria true and try to make false
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return password

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want numbers? (y/n)").lower() == "y"
has_special = input("Do you want special characters? (y/n)").lower() == "y"

test_password = generate_password(min_length, has_number, has_special)
print(test_password)