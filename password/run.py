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


def find_credentials(number):
    '''
    Function that finds a credentials by number and returns the credentials
    '''
    return Credentials.find_by_number(number)


def check_existing_credentials(number):
    '''
    Function that check if a credentials exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(number)


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
    print({auto})
    print("\n-----------------------------------")
    

    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a password, ex -exit the contact list, fe -find a contact")

        short_code = input().lower()
 
        if short_code == 'cc':
            print("New Contact")
            print("-"*10)

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            save_user(create_user(f_name, l_name, p_number, e_address))
            # create and save new contact.
            print('\n')
            print(f"New Contact {f_name} {l_name} created")
            print('\n')
            save_user(create_user(f_name, l_name, p_number, e_address))
            print('\n')
            print(f"New Contact {f_name} {l_name} created")
            print('\n')

        elif short_code == 'dc':
 
            if display_user():
                print(CBLUE+"Here is a list of all your contacts"+CEND)
                print('\n')

                for contact in display_user():
                    print(
                        f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                print('\n')
            else:
                print('\n')
                print(CBLUE+CBOLD+"You dont seem to have any contacts saved yet"+CEND)
                print('\n')
        elif short_code == 'fe':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_user(search_number):
                                    search_contact = find_user(search_number)
                                    print(f"{search_contact.first_name} {search_contact.last_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_contact.phone_number}")
                                    print(f"Email address.......{search_contact.email}")
                            else:
                                    print(CBLUE+CBOLD+"That contact does not exist"+CEND)
        elif short_code == 'fc':

            print(CBLUE+"Enter the number you want to search for"+CEND)

            search_number = input()
            if check_existing_credentials(search_number):
                search_credentials = find_credentials(search_number)
                print(
                    f"{search_credentials.password} {search_credentials.socialSite}")
                print('-' * 20)

                print(f"Phone number.......{search_credentials.password}")
                print(f"Email address.......{search_credentials.socialSite}")
            else:
                print(CBLUE+CBOLD+"That contact does not exist"+CEND)

        elif short_code == "ex":
            print(CBLUE+CBOLD+"Bye ......."+CEND)
            break
        else:
            print(CBLUE+CBOLD+"I really didn't get that. Please use the short codes"+CEND)

       


if __name__ == '__main__':

    main()
