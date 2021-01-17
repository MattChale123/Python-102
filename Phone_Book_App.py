import time

phone_book_entries = {
        'Melissa': '584-3934-5857',
        'Igor': 'You do not contact Igor, Igor contacts you',
        'Jazz': '334-584-2345', 
}

def phone_book_function(phone_book_entries):
    user_input = input('Would you like to: Search, Add, Delete, List All Entries, or Quit? )').lower()
    if (user_input == 'search'):
        user_input_2 = input('Please list name: ').lower().capitalize()
        print(phone_book_entries[user_input_2])
        return phone_book_function(phone_book_entries)
    elif (user_input == 'add'):
        user_input_3 = input('Please enter name: ')
        user_input_4 = input('Please enter phone number: ')
        for key in phone_book_entries:
            adding_entry = {user_input_3: user_input_4}
            phone_book_entries.update(adding_entry)
            return phone_book_function(phone_book_entries)
    elif (user_input == 'delete'):
        user_input_5 = input('What name would you like to delete: ')
        del phone_book_entries[user_input_5]
        return phone_book_function(phone_book_entries)
    elif (user_input == 'list all entries'):
        print(phone_book_entries)
        return phone_book_function(phone_book_entries)
    elif (user_input == 'quit'):
        print('Now quitting.')
        time.sleep(5)
        return
    else:
        print('Please enter Search, Add, Delete, List All Entries, or Quit.')
        return phone_book_function(phone_book_entries)
        

print(phone_book_function(phone_book_entries))