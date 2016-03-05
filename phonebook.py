dictionary = {
    'chris': {'name': 'Chris', 'phone': "503-277-1234"},
    'sam': {'name': 'Sam', 'phone': "503-277-4321"}
}

def main():
    print("Welcome to the Phone Book!")
    while True:
        print("-" * 40)
        print("Press 1 to search.")
        print("Press 2 to add.")
        print("Press 3 to change an entry.")
        print("Press 4 to remove.")
        print("Press 5 to exit.")
        print("-" * 40)
        try:
            choice = int(input('> '))
            if choice == 1:
                search()
            if choice == 2:
                add()
            if choice == 3:
                change()
            if choice == 4:
                remove()
            if choice == 5:
                exit()
        except ValueError:
            print("That is not a valid entry. Please try again.")

def search():
    search_name = input("Who would you like to search for? ").lower()
    try:
        print(dictionary[search_name]["name"])
        print(dictionary[search_name]["phone"])
    except:
        print("That name does not exist in the dictionary.")

def add():
    add_entry_name = input("Who would you like to add? ")
    add_entry_phone = input("What is their number? ")
    dictionary[add_entry_name]= {}
    dictionary[add_entry_name]['name']=add_entry_name
    dictionary[add_entry_name]['phone']=add_entry_phone
    print(dictionary)

def change():
        change_entry_title = input("Who's entry would you like to change? ").lower()
        change_entry_name = input("What should their name be now? ")
        change_entry_number = input("What should their number be now? ")
        try:
            dictionary[change_entry_title]['name']=change_entry_name
            dictionary[change_entry_title]['phone']=change_entry_number
            print(dictionary)
        except:
            print("That entry does not exist.  Try again or add a new entry")

def remove():
    remove_entry = input("Who would you like to remove? ").lower()
    try:
        del dictionary[remove_entry]
        print(dictionary)
    except:
        print("That entry didn't exist to begin with.  Try a different entry.")

main()
