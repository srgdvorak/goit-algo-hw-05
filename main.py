from address_book import AddressBook, Record
from utils import input_error, parse_input


@input_error
def add_contact(args, book: AddressBook):
    name, phone = args
    if name in book:
        book[name].add_phone(phone)
        return "Phone added to existing contact."
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    if name in book and book[name].edit_phone(old_phone, new_phone):
        return "Phone updated."
    return "Phone not found."


@input_error
def show_phones(args, book: AddressBook):
    name = args[0]
    if name in book:
        return "; ".join(p.value for p in book[name].phones)
    return "Contact not found."


def show_all(book: AddressBook):
    return "\n".join(str(record) for record in book.values()) if book else "No contacts."


@input_error
def add_birthday(args, book: AddressBook):
    name, bday = args
    if name in book:
        book[name].add_birthday(bday)
        return "Birthday added."
    return "Contact not found."


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    if name in book and book[name].birthday:
        return str(book[name].birthday)
    return "No birthday set."


def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    return "\n".join(f"{item['name']} - {item['birthday']}" for item in upcoming)


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phones(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()