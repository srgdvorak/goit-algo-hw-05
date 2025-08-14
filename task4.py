def input_error(func):
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
def add_contact(data, contacts):
    name, phone = data.split()
    contacts[name] = phone
    return "Contact added."


@input_error
def get_phone(data, contacts):
    return f"{data}: {contacts[data]}"


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return '\n'.join(f"{n}: {p}" for n, p in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip()
        if user_input.lower() in ("exit", "close"):
            print("Good bye!")
            break

        parts = user_input.split(maxsplit=1)
        command = parts[0].lower()
        data = parts[1] if len(parts) > 1 else ""

        if command == "add":
            print(add_contact(data, contacts))
        elif command == "phone":
            print(get_phone(data, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Unknown command.")