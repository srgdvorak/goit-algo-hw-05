def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    Повертає зрозумілі повідомлення замість винятків.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner


@input_error
def add_contact(args, contacts):
    """
    Додає контакт у словник.
    Очікує два аргументи: ім'я та номер телефону.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def get_phone(args, contacts):
    """
    Повертає телефон за ім'ям.
    """
    name = args[0]
    return f"{name}: {contacts[name]}"


def show_all(contacts):
    """
    Показує всі збережені контакти.
    """
    if not contacts:
        return "No contacts found."
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        command_input = input("Enter a command: ").strip().lower()

        if command_input in ["exit", "close"]:
            print("Good bye!")
            break

        elif command_input == "add":
            user_input = input("Enter a name and phone: ").strip().split()
            result = add_contact(user_input, contacts)
            print(result)

        elif command_input == "phone":
            user_input = input("Enter a name: ").strip().split()
            result = get_phone(user_input, contacts)
            print(result)

        elif command_input == "all":
            result = show_all(contacts)
            print(result)

        else:
            print("Unknown command. Please enter 'add', 'phone', 'all', 'exit' or 'close'.")


if __name__ == "__main__":
    main()