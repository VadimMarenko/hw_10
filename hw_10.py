from collections import UserDict

class Field():
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)    
 
     
class Name(Field):
    pass


class Phone(Field):
    pass


class Record():
    def __init__(self, name: Name, phone=None):
        self.name = name        
        self.phones = []

    def __str__(self):
        return f'{self.name.value}: {self.phones}'
        
    def __repr__(self):
        return str(self.phones)
        
    def add_phone(self, phone):
        if phone:
            self.phones.append(phone)

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        if old_phone in self.phones:
            self.phones.remove(old_phone)
            self.phones.append(new_phone)
            return f"The phone {old_phone} was replaced by {new_phone}"
        else:
            return f"Phone {old_phone} does not exist"



class AddressBook(UserDict):
    def __init__(self, records=None):
        self.records = records
        super().__init__()

    def add_record(self, record: Record):
        if record.name.value not in self.keys():
            self.data[record.name.value] = record            
        else:
            return f"Record {record.name.value} alredy exists"
        return

phone_book = AddressBook({})
name = Name()
phone = Phone()
field = Field()
record = Record(name)


def input_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
        except TypeError: 
            return "Enter the data correctly"
        except KeyError:
            return "Enter the data correctly"
        except ValueError:
            return "Enter the data correctly"
        except IndexError:
            return "Enter the data correctly"

        return result
    return wrapper


def greeting(*args):
    result = "How can I help you?"
    return result


def checking_args(*args):
    if args[0].isalpha():
        name = args[0].capitalize()
        phone = args[1]
        if (phone.startswith("+") and phone[1:].isnumeric()) or phone.isnumeric():            
            pass
        else:       
            return "Give me name and phone please"
    elif args[0].isdigit():
        return "Give me name and phone please"
    

@input_error
def add(*args):
    result = checking_args(*args)
    if result:
        return result
    else:
        name.value = args[0].capitalize()
        phone = args[1]
        record.name = name
        record.add_phone(phone)
        phone_book.add_record(record)
    return f"Added name {name} with phone number {phone}"


input_error
def change(*args): 
    result = checking_args(*args)
    if result:
        return result
    else:
        name = Name(args[0].capitalize())
        phone = Phone(args[1])
        record.name = name
        for key, value in phone_book.items():
            if key == record.name.value:                
                record.change_phone(record.phones[0], phone)                
                return f"{name}'s phone number change to {phone}"


@input_error
def phone(*args):
    if args[0].isalpha:
        name = Name(args[0].capitalize())
        record.name = name
        for key, value in phone_book.items():
            if key == record.name.value:
                record.__str__()
                return f"{name} has phone number {record.phones}"
        else:
            return f"Name '{name}' was not found"
    else:
        return "Give me name please"
        
    
def show(*args):    
    return phone_book


def bye(*args):
    return "Good bye!"


def no_command(*args):    
    return "Unknown command. Supported commands\n\nadd name number\nchange name number\nphone name\nshow all\nexit"


commands = {greeting: ("hello", ),
            add: ("add", ),
            change: ("change", ),
            phone: ("phone", ),
            show: ("show all", ),
            bye: ("good bye", "close", "exit")}


def parser(text: str) -> tuple[callable, tuple[str]|None]:
    for key, value in commands.items():
        for val in value:
            if text.startswith(val):                                
                return key, text.replace(val, "").strip().split()
            
    return no_command, ""


def main():
    while True:
        user_input = input(">>>").lower()
        command, data = parser(user_input)
        result = command(*data)
        print(result)
        if result == "Good bye!":
            break
        

if __name__ == "__main__":
    main()
    