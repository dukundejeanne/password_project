!/usr/bin/env python3.6
from user import User
from user import Credential

def create_user(fname,name,pword,email):
    '''
    function to create a new user account
    '''
    new_user=User(fname,name,pword,email)
    return new_user

def save_user(user):
    '''
    to save a new user account
    '''
    User.save_user(user)

def checks_user(first_name,password):
    '''
    check if the account exist
    '''
    checking_user=Credential.check_user(first_name,password)
    return checking_user

