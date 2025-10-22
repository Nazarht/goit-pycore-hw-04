import readline

user_data = {"contacts": {}}

def parse_input(input_string: str) -> tuple[str, list[str]]:
    command, *args = input_string.split()
    return command, args

def main():
    while True:
        try:
            user_input = input("Enter a command: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            break

        command, args = parse_input(user_input)
        command = command.lower()
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            contact_name = args[0]
            contact_phone_number = args[1]
            user_data["contacts"][contact_name] = contact_phone_number
            print(f"Contact {contact_name} added successfully")
        elif command == "change":
            contact_name = args[0]
            contact_phone_number = args[1]
            user_data["contacts"][contact_name] = contact_phone_number
            print(f"Contact {contact_name} updated successfully")
        elif command == "phone":
            contact_name = args[0]
            print(f"Contact {contact_name} phone number is {user_data['contacts'].get(contact_name, 'not found')}")
        elif command == "all":
            for contact_name, contact_phone_number in user_data["contacts"].items():
                print(f"{contact_name} - {contact_phone_number}")
        elif command in ("exit", "close"):
            print("Good bye!")
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()