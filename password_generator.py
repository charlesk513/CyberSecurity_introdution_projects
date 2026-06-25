import random
import string
print("\nWELCOME TO THE PASSWORD GENERATOR \n")
print("""
      A strong password that is not easily broken by unauthorised personel must meet the following qualities.
      - Atleast 8 characters long
      - Contains both uppercase and lowercase letters
      - Contains special characters (symbols) as represented in the ASCII convention
      - Contains atleast one number\n
      """)
print("Follow the following simple steps to create a random password of your choice\n")
permission = True
while permission:
    choice = input("\nEnter q to exit or any other button to continue: ").lower()
    if choice == "q":
        permission = False
    else:
        try:
            length = int(input("Enter the preffered password length: "))
        except ValueError:
            print("Enter an integer")
            
        print("Password Contains ASCII characters randomly chosen for your preffered length")

        random_password = ""
        for i in range(length):
            random_letter = random.randint(33,128)
            random_password+=chr(random_letter)
        print(f"\nRandom password is: {random_password}")


