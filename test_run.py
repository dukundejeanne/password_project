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
        self.assertEqual(self.new_user.user_name,"marie")
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
    


if __name__=='__main__':
    unittest.main()
