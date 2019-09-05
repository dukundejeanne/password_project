import pyperclip
global user_list
class User:
    """
    class that generates a new instance of a user 
    """
    user_list=[] #empty user list

    def __init__(self,first_name,username,password,email):
        

        self.first_name=first_name
        self.username=username
        self.password=password
        self.email=email

    def save_user(self):
        '''
        save user method saves user objects into user list
        '''
        User.user_list.append(self)
class Credential:
    '''
    class of credential account, generate passwords information
    '''
    credential_list=[]
    user_credential_list=[]

    @classmethod
    def check_user(cls,first_name,password):
        '''
        Method that checks if name and password enteries match
        '''
        current_user=''
        for user in User.user_list:
            if(user.first_name== first_name and user.password==password):
                current_user=user.first_name
        return current_user

    def __init__(self,first_name,site_name,account_name,password):
        '''
        Methode show the properties of user object
        '''
        self.first_name=first_name
        self.site_name=site_name
        self.account_name=account_name
        self.password=password
        

    def save_credential(self):
        '''
        methode to save credential globally
        '''

        Credential.credential_list.append(self)

    @classmethod
    def disp_credential(cls,first_name):
        '''
        method to display all list of saved credentials
        '''
        user_credential_list=[]
        for credential in cls.credential_list:
            if credential.first_name==first_name:
                user_credential_list.append(Credential)
        return user_credential_list
    @classmethod
    def find_site(cls,site_name):
        '''
        Methode that find by site name and return credentials that match
        '''
        for credential in cls.credential_list:
            if credential.site_name==site_name:
                return credential
    
    @classmethod
    def copy_credential(cls,site_name):
        '''
        Methode that copy credential 
        '''
        find_credential=Credential.find_site(site_name)
        return pyperclip.copy(find_credential.password)


    # def delete_user(self):
    #     '''
    #     delete_user method delete a saved used from user
    #     '''
    #     User.user_list.remove(self)
    # @classmethod
    # def find_by_name(cls,username):
    #     '''
    #     method that find by username and return all information that matches

    #     Args:
    #         name: first name to search for 
    #     Returns:
    #         all information of that person
    #     '''
    #     for user in cls.user_list:
    #         if user.username==username:
    #             return user
       
    # @classmethod
    # def user_exist(cls,username):
    #     '''
    #     method that find by username and return all information that matches

    #     Args:
    #         name: first name to search for 
    #     Returns:
    #         all information of that person
    #     '''
    #     for user in cls.user_list:
    #         if user.username==username:
    #             return True
    #     return False
    # @classmethod
    # def display_users(cls):
    #     '''
    #     method that return all user list saved 
    #     '''
        
    #     return cls.user_list
   
    # @classmethod
    # def copy_email(cls,username):
    
    #     user_found=User.find_by_name(username)
    #     pyperclip.copy(user_found.email)

    