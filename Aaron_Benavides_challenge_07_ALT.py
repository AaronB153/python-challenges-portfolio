'''

Challenge 07

Checking for Common Passwords


For this challenge, you will be writing a program that stores 
50 of the most common passwords (contained at the end of this instruction page) 
in a tuple (since they are immutable).  You will then ask the user to create a 
username and password using a looping structure OR the in operator, check if the 
user's password is stored in the list, and IF it is, print out:
"Your password is too common.  Please consider changing it."  
If the password is not in the list, then print out:  "You have a strong password."  
Finally, you will need to print out the location in the tuple where the password is 
stored if one was already found, i.e  at index 0, 10, 50. 

Programming constructs allowed to be used:

Tuples and Lists (Though you are specifically using a Tuple here, not a List)
Loops (probably a for loop for this) IF you don't use the in operator.
In operator
Decision Structures (IF, ELIF, ELSE)
Comparing strings
processing input
Index locations

'''

def stored_passwords(password): #invalid passwords stored here
    check_pass = ('123456', '123456789', '12345', 'qwerty',
                  'password', '12345678', '111111', '123123', '1234567890',
                  '1234567', 'qwerty123', '000000', '1q2w3e', 'aa12345678', 
                  'abc123', 'password1', '1234', 'qwertyuiop', '123321', 
                  'password123', '1q2w3e4r5t', 'iloveyou', '654321', '666666', 
                  '987654321', '123', '123456a', 'qwe123', '1q2w3e4r', '7777777', 
                  '1qaz2wsx', '123qwe', 'zxcvbnm', '121212', 'asdasd', 
                  'a123456', '555555', 'dragon', '112233', '123123123',
                  'monkey', '11111111', 'qazwsx', '159753', 'asdfghjkl', 
                  '222222', '1234qwer', 'qwerty1', '123654', '123abc')
    
    if password in check_pass:  #check tuple for user iput and return results
            return "invalid", check_pass.index(password) 
    else:
            return "valid", []




def get_user_pass():    #we will get user input here and pass it to "stored_passwords()"
    username = str(input("Create a username: "))
    while True:         #this loop will keep calling "stored_passwords()" 
                        #until the user makes a valid password
        password = str(input("Create your password: "))
        result, index = stored_passwords(password)
        
        if result == "invalid":
                print((f"\nYour password is too common, "
                    "please consider changing it.\n"
                    f"Found in index position {index}"))
        elif result == "valid":
                print("\nYou have a strong password."
                      "\nThese are your credentials:\n")
                break
    
    print(f"New username: {username}")
    print(f"New password: {password}\n")
    
    
    





if __name__ == "__main__":
    get_user_pass()