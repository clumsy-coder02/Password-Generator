# modules used
import random 

# intro the project
print() # spacing
print("***Jumbled Up Password Generator***")
print() # spacing

# get details
print("Select the Type of Password")
print("\n1.Numeric password\n2.Alphabetical password\n3.Alphanumeric password\n4.I don't need a password")
print() # spacing
password_type = input("Select by typing a number: ")

# main function
def select_options():
    if password_type == "1":
        # call the numeric function
        numeric_password() 
    elif password_type == "2":
        # call the alphabetical function
        alphabetical_password()
    elif password_type == "3":
        # alphanumeric function
        alphanumeric_password()
    elif password_type == "4":
        # call the exit function
        exit_program()
    else:
        # inform the user to select from the options above
        instructions()


# functions
# numeric function

def numeric_password():
    password_length = int(input("Enter the length of password: "))
    password = "" # final password output as a string
    
    # Generate random digits for the specified length
    numeric_index = 1
    while numeric_index < password_length:
        password += str(random.randint(0, 100)) # random value as a string
        numeric_index+=1  # prevent infinite loop  

    print(f"\nYour password: {password}")

            
# alphabetical password
def alphabetical_password():
    password_length = int(input("Enter the length of password: "))
    password = "" # final password output as a string

    # Generate random letters
    letters_index = 1
    while letters_index < password_length:
        letter_sequence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password += random.choice(letter_sequence)
        letters_index+=1 # prevent infinite loop
    
    print(f"\nYour password: {password}")

     

# alphanumeric password
def alphanumeric_password():
    password_length = int(input("Enter the length of password: "))
    numeric_password = "" # number values
    alphabetic_password = "" # alphabetical password
    password = "" # final password output as a string

    # generate random numbers, half of the password length
    numeric_index = 1
    while numeric_index < password_length // 2:
        numeric_password += str(random.randint(0,100)) # random value as a string
        numeric_index+=1 # prevent infinite loop
    
    # generate random letters, half of the password length
    letters_index = 1
    while letters_index < password_length // 2:
        letter_sequence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabetic_password += random.choice(letter_sequence)
        letters_index+=1 # prevent infinite loop
    
    # combine the two values & convert into a list for shuffle to work
    combined_values = list(numeric_password + alphabetic_password)
    # mix the values up 
    random.shuffle(combined_values)
    # convert to a string
    password += "".join(combined_values)

    print(f"Your password: {password}")



# exit program
def exit_program():
    exit()

# instructions function
def instructions():
    print() # spacing 
    print("Follow Instructions 🤬🤦‍♂️")
    print() # spacing
    message = print("""You're reading this because you can't follow simple instructions;
    \nWhen i asked 'Select the type of password': you reply by typing the numbers 1 to 4.
    \nType 1 if you want the script to generate a numeric password(password with only numbers).
    \nType 2 if you want the script to generate an alphabetical password(password made up of small and capital letters).
    \nType 3 if you want the script to generate a mix of the two above.
    \nFinally type 4 to exit the program""")
    return message


# run code as script or module
if __name__ == "__main__":
    select_options() # function to run first