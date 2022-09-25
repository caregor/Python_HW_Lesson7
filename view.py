import model
def mode():
    choose_mode = input('What you want to do(1- add new contact; 2- find existing contact):')
    return choose_mode


def get_contact():
    return input('Enter last name: ')


def import_contact():
    contact = list(map(str, input('Enter Name Last name Phone Description: ').split()))
    mod_contact = model.preparing_data(contact)
    print('mod contact',mod_contact)
    prepare_contact = dict(zip(('first_name', 'last_name', 'phone', 'description'), mod_contact))
    return prepare_contact
