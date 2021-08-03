#!/usr/bin/env python
from user import User
from credentials import Credentials

#! shebang



'''
users
'''
def create_user(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_user = User(fname,lname,phone,email)
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
def create_credentials(password,socialSite):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(password,socialSite)
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
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_user(create_user(f_name,l_name,p_number,e_address)) 
                             # create and save new contact.
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')
                            save_user(create_user(f_name,l_name,p_number,e_address))
                            print ('\n')
                            print(f"New Contact {f_name} {l_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_user():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_user():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_credentials(search_number):
                                    search_credentials = find_credentials(search_number)
                                    print(f"{search_credentials.password} {search_credentials.socialSite}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_credentials.password}")
                                    print(f"Email address.......{search_credentials.socialSite}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

    main()