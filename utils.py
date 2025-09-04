from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return True
        return False

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        phones = "; ".join(str(p) for p in self.phones)
        bday = f", Birthday: {self.birthday}" if self.birthday else ""
        return f"{self.name.value}: {phones}{bday}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def get_upcoming_birthdays(self):
        today = datetime.now().date()
        end_date = today + timedelta(days=7)
        upcoming = []

        for record in self.data.values():
            if record.birthday:
                bday_this_year = record.birthday.value.replace(year=today.year)

                if today <= bday_this_year <= end_date:
                    greeting_date = bday_this_year
                    if greeting_date.weekday() >= 5:  # Saturday or Sunday
                        days_to_monday = 7 - greeting_date.weekday()
                        greeting_date += timedelta(days=days_to_monday)

                    upcoming.append({
                        "name": record.name.value,
                        "birthday": greeting_date.strftime("%d.%m.%Y")
                    })

        return upcoming