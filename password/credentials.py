import pyperclip
class Credentials:
    """
    Class that generates new instances of credentials.
    """
    credentials_list = []  # Empty credentials list

    def __init__(self,password, socialSite):

      # docstring removed for simplicity

        self.password = password
        self.socialSite = socialSite

    credentials_list = []  # Empty credentials list
 # Init method up here

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)
    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)
    
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a credentials that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            credentials of person that matches the number.
        '''

        for credentials in cls.credentials_list:
            if credentials.password == number:
                return credentials

    @classmethod
    def credentials_exist(cls,number):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.password == number:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def copy_socialSite(cls,number):
        credentials_found = Credentials.find_by_number(number)
        pyperclip.copy(credentials_found.socialSite)