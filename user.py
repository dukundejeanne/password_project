class User:
    """
    class that generates a new instance of a user 
    """
    user_list=[] #empty user list

    def __init__(self,first_name,user_name,password,email):
        #docstring removed for simplicity

        self.first_name=first_name
        self.user_name=user_name
        self.password=password
        self.email=email

    def save_user(self):
        '''
        save user method saves user objects into user list
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user method delete a saved used from user
        '''
        User.user_list.remove(self)
    pass