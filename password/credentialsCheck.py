import unittest # Importing the unittest module
from credentials  import Credentials  # Importing the credentials  class
import pyperclip
class TestCredentials (unittest.TestCase):

    '''
    Test class that defines test cases for the credentials  class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials  = Credentials ("0712345678","james@ms.com") # create credentials  object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.password,"0712345678")
        self.assertEqual(self.new_credentials .socialSite,"james@ms.com")
    def test_save_credentials (self):
        '''
        test_save_credentials  test case to test if the credentials  object is saved into
         the credentials  list
        '''
        self.new_credentials .save_credentials () # saving the new credentials 
        self.assertEqual(len(Credentials .credentials_list),1)
    # Items up here...

    def test_save_multiple_credentials (self):
            '''
            test_save_multiple_credentials  to check if we can save multiple credentials 
            objects to our credentials_list
            '''
            self.new_credentials .save_credentials ()
            test_credentials  =Credentials ( "0712345678","test@user.com") # new credentials 
            test_credentials .save_credentials ()
            self.assertEqual(len(Credentials .credentials_list),2)
    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials .credentials_list = []

# other test cases here
    def test_save_multiple_credentials (self):
            '''
            test_save_multiple_credentials  to check if we can save multiple credentials 
            objects to our credentials_list
            '''
            self.new_credentials .save_credentials ()
            test_credentials  =Credentials ( "0712345678","test@user.com") # new credentials 
            test_credentials .save_credentials ()
            self.assertEqual(len(Credentials .credentials_list),2)
    # More tests above
    def test_delete_credentials (self):
            '''
            test_delete_credentials  to test if we can remove a credentials  from our credentials  list
            '''
            self.new_credentials .save_credentials ()
            test_credentials  =Credentials ( "0712345678","test@user.com") # new credentials 
            test_credentials .save_credentials ()

            self.new_credentials .delete_credentials ()# Deleting a credentials  object
            self.assertEqual(len(Credentials .credentials_list),1)
    def test_find_credentials_by_number(self):
        '''
        test to check if we can find a credentials  by phone number and display information
        '''

        self.new_credentials .save_credentials ()
        test_credentials  =Credentials ( "0711223344","test@user.com") # new credentials 
        test_credentials .save_credentials ()

        found_credentials  = Credentials.find_by_number("0711223344")

        self.assertEqual(found_credentials .socialSite,test_credentials .socialSite)
    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials .
        '''

        self.new_credentials .save_credentials ()
        test_credentials  =Credentials ( "0711223344","test@user.com") # new credentials 
        test_credentials .save_credentials ()

        credentials_exists = Credentials .credentials_exist("0711223344")

        self.assertTrue(credentials_exists)
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials s saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials .credentials_list)
    def test_copy_socialSite(self):
        '''
        Test to confirm that we are copying the socialSite address from a found credentials 
        '''

        self.new_credentials .save_credentials ()
        Credentials .copy_socialSite("0712345678")

        self.assertEqual(self.new_credentials .socialSite,pyperclip.paste())
if __name__ == '__main__':
    unittest.main()