#import module
import string
import random
#Define Character Set
characters = string.ascii_letters + string.digits + string.punctuation 
#Create Password Generator Function
def generate_password(length=12) :
    password = ""
    for i in range(length) :
        password+=random.choice(characters)
    return password
#Add Input handling
def password_generator() :
     print ("Christian's password generator")

length = int(input("How many characters are needed for your password?"))
if length <6:
    print("password length should be at least 4 characters")
else:
    password= generate_password(length)
    print(f"Your password is : {password}")

# Run the Program
password_generator()    
