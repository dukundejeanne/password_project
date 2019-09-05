import unittest 
from user import User
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
    def tearDown(self):
        '''
        tear down method that does clean after each test case.
        '''
        User.user_list=[]
    def test_save_multiple_user(self):
        '''
        to check if we can save multiple user information
        '''
        self.new_user.save_user()
        test_user=User("Test","user","password","test@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_contact(self):
        '''
        delete user to test if we can delete a user
        '''
        self.new_user.save_user()
        test_user=User("Test","user","password","test@user.com")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_name(self):
        '''
        test to check if we can find the user name and display information
        '''

        self.new_user.save_user()
        test_user=User("Test","user","password","test@user.com")
        test_user.save_user()

        found_user=User.find_by_name("user")

        self.assertEqual(found_user.email,test_user.email)

    def test_user_exists(self):
        '''
        test if we ca return our user information
        '''
        self.new_user.save_user()
        test_user=User("Test","user","password","test@user.com")
        test_user.save_user()
        
        user_exists=User.user_exist("user")
        self.assertTrue(user_exists)

    def test_display_all_users(self):
        '''
        method to display all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)
    


if __name__=='__main__':
    unittest.main()
