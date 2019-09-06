#!/usr/bin/env python3.6
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

def create_cred(first_name,site_name,account_name,password):
    '''
    new credential account
    '''
    new_credential=Credential(first_name,site_name,account_name,password)
    return new_credential
def save_credential(credential):
    '''
    to save all credentials
    '''
    Credential.save_credential(credential)




