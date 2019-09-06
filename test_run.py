

import unittest 
from user import User
from user import Credential
import pyperclip

class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for the user class

    Args:
        unittest,TestCase: TestCase class that helps in creating test
    '''
    def setUp(self):
        '''
        set up method of test case
        '''
        self.new_user=User("jeanne","marie","dukunde","dukunde@gmail.com")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"jeanne")
        self.assertEqual(self.new_user.username,"marie")
        self.assertEqual(self.new_user.password,"dukunde")
        self.assertEqual(self.new_user.email,"dukunde@gmail.com")
    def test_save_user(self):
        '''
        to test if the user object information is saved into a list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1) 

class TestCredentials(unittest.TestCase):
    '''
    class that test the credential 

    Args:
        unittest and test case help in creating test for our credential
    '''

    def test_check_user(self):
        '''
        methode to check if our user login work
        '''
        self.new_user=User("jeanne","marie","dukunde","dukunde@gmail.com")
        self.new_user.save_user()
        userOne=User("jeanne","marie","dukunde","dukunde@gmail.com")
        userOne.save_user()

        # current_user=''
        for user in User.user_list:
            if user.first_name == userOne.first_name and user.password==userOne.password:
                current_user=user.first_name
        return current_user

        self.assertEqual(current_user,Credential.check_user(userOne.password,userOne.first_name))
    
    def setUp(self):
        
        '''
        set up method of test case
        '''
        self.new_credential=Credential("jeanne","facebook","dukunde","dukunde")

    def test__init(self):
        '''
        test_init test case to test if the object is initialized properly for credential
        '''
        self.assertEqual(self.new_credential.first_name,'jeanne')
        self.assertEqual(self.new_credential.site_name,"facebook")
        self.assertEqual(self.new_credential.account_name,"dukunde")
        self.assertEqual(self.new_credential.password,"dukunde")

    def test_save_credentials(self):
        '''
        method which test to save credential
        '''

        self.new_credential.save_credential()
        twitter=Credential("jeanne","Twitter","dukunde","dukunde")
        twitter.save_credential()
        self.assertEqual(len(Credential.credential_list),2)


    def tearDown(self):
        '''
        tear down method that does clean after each test case.
        '''
        User.user_list=[]
        Credential.credential_list=[]

    def test_disp_credential(self):
        '''
        method to check if display works
        '''

        self.new_credential.save_credential()
        twitter=Credential("jeanne","facebook","dukunde","dukunde")
        twitter.save_credential()
        gmail=Credential("jeanne","gmail","dukunde","dukunde1")
        gmail.save_credential()
        self.assertEqual(len(Credential.disp_credential(twitter.first_name)),3)

    def test_find_site(self):
        '''
        Methode to find by site name and retun the correct credentials
        '''
        self.new_credential.save_credential()
        twitter=Credential("jeanne","Twitter","dukunde","dukunde")
        twitter.save_credential()
        credential_exists=Credential.find_site('Twitter')
        self.assertEqual(credential_exists,twitter)

    def test_copy(self):
        '''
        Methode to copy the credential and save them
        '''

        self.new_credential.save_credential()
        twitter =Credential("jeanne","Twitter","dukunde","dukunde")
        twitter.save_credential()
        find_credential=None
        for credential in Credential.user_credential_list:

            find_credential=Credential.find_site(credential.site_name)
            return pyperclip.copy(find_credential.password)

        Credential.copy_credential(self.new_credential.site_name)
        self.assertEqual('dukunde',pyperclip.paste())
        print(pyperclip.paste())

# if __name__=='__main__':
#     unittest.main(verbosity=2)



            # def test_save_multiple_user(self):
    #     '''
    #     to check if we can save multiple user information
    #     '''
    #     self.new_user.save_user()
    #     test_user=User("Test","user","password","test@user.com")
    #     test_user.save_user()
    #     self.assertEqual(len(User.user_list),2)

    # def test_delete_contact(self):
    #     '''
    #     delete user to test if we can delete a user
    #     '''
    #     self.new_user.save_user()
    #     test_user=User("Test","user","password","test@user.com")
    #     test_user.save_user()

    #     self.new_user.delete_user()
    #     self.assertEqual(len(User.user_list),1)

    # def test_find_user_by_name(self):
    #     '''
    #     test to check if we can find the user name and display information
    #     '''

    #     self.new_user.save_user()
    #     test_user=User("Test","user","password","test@user.com")
    #     test_user.save_user()

    #     found_user=User.find_by_name("user")

    #     self.assertEqual(found_user.email,test_user.email)

    # def test_user_exists(self):
    #     '''marie
    #     test if we ca return our user information
    #     '''
    #     self.new_user.save_user()
    #     test_user=User("Test","user","password","test@user.com")
    #     test_user.save_user()
        
    #     user_exists=User.user_exist("user")
    #     self.assertTrue(user_exists)

    # def test_display_all_users(self):
    #     '''
    #     method to display all users saved
    #     '''

    #     self.assertEqual(User.display_users(),User.user_list)
    # def test_copy_email(self):
    #     '''
    #     test to copy the email address from a found
    #     '''

    #     self.new_user.save_user()
    #     User.copy_email("marie")

    #     self.assertEqual(self.new_user.email,pyperclip.paste())


if __name__=='__main__':
    unittest.main()
