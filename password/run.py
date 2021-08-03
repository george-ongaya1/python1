#!/usr/bin/env python
from user import User
from credentials import Credentials
import random
import string
 

#! shebang


'''
users
'''
 


def create_user(fname, lname, phone, email):
    '''
    Function to create a new contact
    '''
    new_user = User(fname, lname, phone, email)
    return new_user


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


def find_user(number):
    '''
    Function that finds a user by number and returns the user
    '''
    return User.find_by_number(number)


def check_existing_user(number):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(number)


def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

'''
credentials
'''


def create_credentials(password, socialSite):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(password, socialSite)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()


def find_credentials(numbe):
    '''
    Function that finds a credentials by number and returns the credentials
    '''
    return Credentials.find_by_number(numbe)


def check_existing_credentials(numbe):
    '''
    Function that check if a credentials exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(numbe)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


'''
main application
'''


def main():
    CBOLD= '\33[1m' 
    CWHITE ='\33[37m'
    CEND ='\033[0m'
    CREDBG='\33[41m'
    CBLUE= '\33[94m'
    CGREEN2  = '\33[92m'
  
    print("\n-----------------------------------")
    print(CREDBG+CWHITE+CBOLD+"Hello Welcome to your user list. What is your name?"+CEND)
    print("\n-----------------------------------")
    user_name = input()
    
#colors in use
#CBLUE= '\33[94m'     
#CGREENBG  = '\33[42m'
#CYELLOWBG = '\33[43m'
#CBLUEBG   = '\33[44m'
#CVIOLETBG = '\33[45m'
#CBEIGEBG  = '\33[46m'
#CWHITEBG  = '\33[47m'
#CGREEN2  = '\33[92m'
#CYELLOW2 = '\33[93m'
#CBLUE2   = '\33[94m'
#CBEIGE  = '\33[36m'
    

#password generator
    print("\n-----------------------------------")
    print(CREDBG+CWHITE+"Have a complimentary auto-password"+CEND)
    length=int(input('\nEnter the desired length of password::  '))
    
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    num=string.digits
    symbols=string.punctuation

    all=lower+upper+num+symbols
    temp=random.sample(all,length)
    autopassword="".join(temp)
    auto=autopassword

    print(f"Hello {user_name}. what would you like to do?")
   
    
    
    print("\n-----------------------------------")
    print(CBLUE+"Feel free to use the password :: "+CEND)
    print(auto)
    print("\n-----------------------------------")
    

    while True:
        print(CGREEN2+CBOLD+"""Use these short codes : 
        cc -create a new contact            fe -find a contact
        dc -display contacts                ff -create new credentials
        fc -search credentials              fg -display credentials
        ex -exit the contact list      
        """+CEND)

        short_code = input().lower()
 
        if short_code == 'cc':
            print("New Contact")
            print("-"*10)

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("phone ...")
            phone = input()

            print("lemai ...")
            email = input()

            

           
            save_user(create_user (f_name, l_name,phone,email))
            # create and save new contact.
            print('\n')
            print(f"New Contact {f_name} {l_name} created")
            print('\n')
            save_user(create_user (f_name, l_name,phone,email))
            print('\n')
            print(f"New Contact {f_name} {l_name} created")
            print('\n')

        elif short_code == 'ff':
            print('\n')
            print("New Credentials")
            print("-"*10)

            print("Social site ....")
            socialSite = input()

            print("password ...")
            password= input()

            save_credentials(create_credentials(socialSite, password))
            # create and save new credential.
            print('\n')
            print(f"New SocialSite{socialSite} {password} created")
            print('\n')
            save_credentials(create_credentials(socialSite, password))
            print('\n')
            print("New credential")
            print(f"New social site:{socialSite}")
            print('\n')
            print(f"New Password:{password} created")
            print('\n')


        elif short_code == 'dc':
 
            if display_user():
                print(CBLUE+"Here is a list of all your users"+CEND)
                print('\n')

                for user in display_user():
                    print(
                        f"{user.f_name} {user.l_name} ....{user.phone}")

                print('\n')
            else:
                print("\n-----------------------------------")
                print(CBLUE+CBOLD+"You dont seem to have any users saved yet"+CEND)
                print("\n-----------------------------------")
           
        elif short_code == 'fg':
 
            if display_credentials():
                print(CBLUE+"Here is a list of all your credentials"+CEND)
                print('\n')

                for credentials in display_credentials():
                    print(
                        f"{credentials.socialSite} {credentials.password} .....{credentials.numbe}")

                print('\n')
            else:
                print("\n-----------------------------------")
                print(CBLUE+CBOLD+"You dont seem to have any credentials saved yet"+CEND)
                print("\n-----------------------------------")
               
        elif short_code == 'fe':

                            print("Enter the user you want to search for")

                            search_number = input()
                            if check_existing_user(search_number):
                                    search_user = find_user(search_number)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"first name.......{search_user.first_name}")
                                    print(f"last name.......{search_user.last_name}")
                            else:
                                    print("\n-----------------------------------")
                                    print(CBLUE+CBOLD+"That user does not exist"+CEND)
                                    print("\n-----------------------------------")
                                    
        elif short_code == 'fc':

            print(CBLUE+"Enter the credential you want to search for"+CEND)

            search_numbe = input()
            if check_existing_credentials(search_numbe):
                search_credentials = find_credentials(search_numbe)
                print(
                    f"{search_credentials.password} {search_credentials.socialSite}")
                print('-' * 20)

                print(f"password.......{search_credentials.password}")
                print(f"socialSite.......{search_credentials.socialSite}")
            else:
                print("\n-----------------------------------")
                print(CBLUE+CBOLD+"That credential does not exist"+CEND)
                print("\n-----------------------------------")

        elif short_code == "ex":
            print(CBLUE+CBOLD+"Bye ......."+CEND)
            break
        else:
            print("\n-----------------------------------")
            print(CBLUE+CBOLD+"I really didn't get that. Please use the short codes"+CEND)
            print("\n-----------------------------------")

       


if __name__ == '__main__':

    main()
