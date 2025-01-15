# Декоратор для обробки помилок вводу
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid command. Please provide valid arguments."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command. Not enough arguments."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
    return inner

# Функція для розбору вводу користувача на команду та аргументи.
def parse_input(user_input): 
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Функція для додавання нового контакту
@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide both name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Функція для зміни номера телефону існуючого контакту
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide both name and new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

# Функція для показу номера телефону за ім'ям
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Please provide a name."
    name = args[0]
    if name in contacts:
        return f"The phone number of {name} is {contacts[name]}."
    else:
        return "Contact not found."

# Функція для показу всіх контактів
@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    contact_list = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return contact_list

# Основна функція
def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

# Запуск бота
if __name__ == "__main__":
    main()
