# password strength checker
# using the regular expression (re) module

import re
#the conditions to chek the strength of passwords
#min 8 chars, digit, uppercase, lowercase & special charecter

def check_password_strength(password):   #password is the parameter
    if len(password) < 8: # checking the length
        return " Your password is weak!!.please enter min 8 chars"
    
    if not any(char.isdigit() for char in password):
        return "Your password is weak!!.it must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "Your password is weak!!.it should contain a uppercase char"

    if not any(char.islower() for char in password):
        return "Your password is weak!!.it should contain a lowercase char"
        
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."
    
    return "strong!!. your password is secured"

def password_checker():
    print("welcome! to password strength checker!")

    while True:

        password = input("Enter your password:")


        if password.lower() == 'exit':
            print("Thank you for using this!")
            break
        result = check_password_strength(password)
        print(result)

#run the password checker tool
if __name__ =="__main__":
    password_checker()
