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

def disp_credential(first_name):
    '''
    to display all credentials stored
    '''
    return Credential.disp_credential(first_name)

def copy_credential(site_name):
    '''
    function to copy credentials 
    '''
    return Credential.copy_credential(site_name)

def main():
    print(' ')
    print('welcome to the password Locker application')
    while True:
        print(' ')
        print("-"*60)
        print("use these codes to navigate: \n ca - Create account \n li - Login \n ex - Exit")

        short_code = input('Please Enter your choice:').lower().strip()
        if short_code == 'ex':
            break
        elif short_code == 'ca':
            
            print("-"*60)
            print(' ')
            print("Create a new account:")
            first_name=input('Enter First_name: ').strip()
            username=input('Enter the Username: ').strip()
            password=input('Enter the Password: ').strip()
            email=input('Enter your Email: ').strip()
            save_user(create_user(first_name,username,password,email))
            print(" ")
            print(f'{first_name} {username} {email} {password} created successfully ')
        elif short_code == 'li':
            print("-"*60)
            print(' ')
            print("Login account:")
          
            username=input('Enter your Username: ').strip()
            password=str(input('Enter the Password: '))
            user_exists== checks_user(first_name,username,password,email)
            if user_exists == first_name:
                print(" ")
                print(f'Welcome {first_name}.Please choose to continue.')
                print('')
                while True:
                    print("-"*60)
                    print('Navigation code: \n cc-Create a Credential \n dc-Display Credentials \n cp-Copy Password \n ex-Exit')
                    short_code=input('Please Enter your choice: ').lower().strip()
                    print("-"*60)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Bye {first_name}')
                        break
                    elif short_code =='cc':
                        print(' ')
                        print('Enter your credential: ')
                        site_name=input('enter the site name\'s name-').strip()
                        account_name=input('Enter your account\'s name- ').strip()
                        while True:
                            print(' ')
                            print("-"*60)
                            print('Please choose any option:\n ep-enter existing password \n ng-generate a password \n ex-exit')
                            pass_choice=input('Enter your option: ').lower().strip()
                            print("-"*60)
                            if pass_choice== 'ep':
                                print(" ")
                                password =input('Enter your password: ').strip()
                                break
                            elif pass_choice == 'ex':
                                break
                            elif pass_choice == 'gp':
                                password=generate_password()
                            else:
                                print('sorry!!! Wrong option and  Try again ')
                        save_credential(create_cred(first_name,site_name,account_name,password,email))
                        print(' ')
                        print(f'Credential Created !!! Site Name: {site_name} -Account Name: {account_name} - Password: {password}- Email: {email}')
                        print('')
                    elif short_code == 'dc':
                        print(' ')
                        if disp_credential(first_name):
                            print('List of Credentials')
                            print(' ')
                            for credential in disp_credential(first_name):
                                print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password} - Email: {credential.email}')
                            print(' ')

                        else:
                                print(' ')
                                print(" you don't have any credential ")
                                print('')
                    elif short_code == 'cp':
                        print(' ')
                        chosen_site= input('Enter the site name to copy : ')
                        copy_credential(chosen_site)
                        print(' ')
                    else:
                        print('Wrong option!! Try again.')

            else:
                print(' ')
                print("try again or create an account")

        else:
            print("-"*60)
            print(' ')
            print(' Wrong option try Again.')
                           



if __name__ == '__main__':
    main()




