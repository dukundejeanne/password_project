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
    def delete_user(self):
        '''
        delete_user method delete a saved used from user
        '''
        User.user_list.remove(self)
    @classmethod
    def find_by_name(cls,username):
        '''
        method that find by username and return all information that matches

        Args:
            name: first name to search for 
        Returns:
            all information of that person
        '''
        for user in cls.user_list:
            if user.username==username:
                return user
    
    pass