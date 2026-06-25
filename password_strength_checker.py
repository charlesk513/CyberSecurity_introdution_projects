print("\nWELCOME TO THE PASSWORD STRENGTH CHECKER\n")
print("""
      A strong password that is not easily broken by unauthorised personel must meet the following qualities.
      - Atleast 8 characters long
      - Contains both uppercase and lowercase letters
      - Contains special characters as represented in the ASCII convention
      - Contains atleast one number\n
      """)
permission = True
while(permission):
    user_input = input("\nPlease enter password for strength evaluation: ")
    up = user_input.upper()
    low = user_input.lower()
    
    if user_input == "q":
        break
    #length checker
    length = len(user_input)
    
    # upper or lower case check
    upper_lower = False
    if(user_input == up) or (user_input == low):
        pass
    else:
        upper_lower = True
    
    #checking for a special character
    count_char = 0
    count_num = 0
    for i in user_input:
        if not i.isalnum():
            count_char+=1
            count_num+=1
    
            
    #evaluation 
    if (length > 8) and upper_lower and count_char >= 3 and count_num >= 3:
        print("\nStrong Password")
        print(f"""
              - character length is {length} 
              - contains both upper and lower case letters
              - has {count_char} special characters
              - has {count_num} digits in it
              """)
    elif (length >= 8) and  upper_lower and count_char > 0 and count_num > 0:
        print("\nMedium Password")
        print(f"""
              - character length is {length} 
              - contains both upper and lower case letters
              - has {count_char} special characters
              - has {count_num} digits in it
              """)
    elif count_num > 0 and (upper_lower  or length == 7 or length == 6):
        print("\nWeak Password")
        if(upper_lower):
            print(f"""
                - character length is {length} 
                - has {count_char} special characters
                - has {count_num} digits in it
                - contains both upper and lower case letters
                """)
        else:
            print(f"""
                - character length is {length} 
                - has {count_char} special characters
                - has {count_num} digits in it
                """)
    elif (length <= 5) or upper_lower:
        print("Very weak Password")
    else:
        print("EEhhhhh, very fake password")
    
    if(length < 8): 
        print("Please enter password atleast 8 characters long")
    if count_char == 0:
        print("Include atleast a special character")
    if count_char == 0:
        print("Include atleast a special character")
    if(user_input == up):
        print("\nThe password entered must have atleast one lower case letter")
    elif(user_input == low):
        print("\nThe password entered must have atleast one upper case letter")
    
    print("TRY AGAIN")
    