# modules used
import random 

# intro the project
print() # spacing
print("***Jumbled Up Password Generator***")
print() # spacing

# get details
print("Select the Type of Password")
print("\n1.Numeric password\n2.Alphabetical password\n3.Alphanumeric password\n4.Complex password\n5.I don't need a password")
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
        # call the complex password function
        complex_password()
    elif password_type == "5":
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
    while numeric_index <= password_length:
        password += str(random.randint(0, 9)) # random value as a string
        numeric_index+=1  # prevent infinite loop  

    print(f"\nYour password: {password}")

            
# alphabetical password
def alphabetical_password():
    password_length = int(input("Enter the length of password: "))
    password = "" # final password output as a string

    # Generate random letters
    letters_index = 1
    while letters_index <= password_length:
        letter_sequence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        password += random.choice(letter_sequence)
        letters_index+=1 # prevent infinite loop
    
    print(f"\nYour password: {password}")

     

# alphanumeric password
def alphanumeric_password():
    password_length = int(input("Enter the length of password: "))
    numeric_password = "" # number values
    alphabetic_password = "" # alphabetical password

    random_password = "" # template of final password
    password = "" # final password output as a string

    # generate random numbers, same number as the password length
    numeric_index = 1
    while numeric_index <= password_length:
        numeric_password += str(random.randint(0,9)) # random value as a string
        numeric_index+=1 # prevent infinite loop
    
    # generate random letters, same number as password length
    letters_index = 1
    while letters_index <= password_length:
        letter_sequence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabetic_password += random.choice(letter_sequence)
        letters_index+=1 # prevent infinite loop
    
    # combine the two values, resulting in twice the password length
    combined_values = numeric_password + alphabetic_password

    # select randomly, same number of password length
    random_select_index = 1
    while random_select_index <= password_length:
        # sequence is the combined values
        random_password += random.choice(combined_values)
        random_select_index+=1 # prevent infinite loop
    
    # convert into a list for mixing to work
    random_password_list = list(random_password)
    # mix the values up 
    random.shuffle(random_password_list)
    # convert to a string
    password += "".join(random_password_list)

    print(f"Your password: {password}")

# complex password
def complex_password():
    # quarter numbers, quarter special characters(full half of password length), half letters
    password_length = int(input("Enter the length of password: "))

    numeric_password = "" # number values
    letters_password = "" # letter values, small & capital

    random_password = "" # template for final password
    password = "" # main output 

    # generate random numbers, same number of the password length
    numeric_index = 1
    while numeric_index <= password_length:
        numeric_password += str(random.randint(0,9))
        numeric_index+=1 # prevent infinite loop
    
    # generate random letters and special characters 1/2 of the password
    letters_index = 1
    while letters_index <= password_length:
        letters_sequence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#%^&*"
        letters_password += str(random.choice(letters_sequence))
        letters_index+=1 # prevent infinite loop

    # combine all passwords, resulting in twice the password length
    combined_values = numeric_password + letters_password

    # select randomly, same number as password length
    random_select_index = 1
    while random_select_index <= password_length:
        # the sequence is the combined values
        random_password += random.choice(combined_values)
        random_select_index+=1 # prevent infinite loop
    
    # convert the password template into a list
    random_password_list = list(random_password)
    # mix them up
    random.shuffle(random_password_list)
    # convert them back to a string and add to the main output
    password += "".join(random_password_list)

    # display final output
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