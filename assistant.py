import readline
from collections import defaultdict

def main():
    contacts: defaultdict[str, str] = defaultdict(lambda: 'not found')
    
    def parse_input(input_string: str) -> tuple[str, list[str]]:
        command, *args = input_string.split()
        return command, args

    def handle_hello(_: list[str]) -> None:
        print("How can I help you?")

    def handle_add(args: list[str]) -> None:
        if len(args) < 2:
            print("Please provide name and phone number")
            return
        contact_name = args[0]
        contact_phone_number = args[1]
        contacts[contact_name] = contact_phone_number
        print(f"Contact {contact_name} added successfully")

    def handle_change(args: list[str]) -> None:
        if len(args) < 2:
            print("Please provide name and new phone number")
            return
        contact_name = args[0]
        contact_phone_number = args[1]
        contacts[contact_name] = contact_phone_number
        print(f"Contact {contact_name} updated successfully")

    def handle_phone(args: list[str]) -> None:
        if len(args) < 1:
            print("Please provide a contact name")
            return
        contact_name = args[0]
        print(
            f"Contact {contact_name} phone number is {contacts.get(contact_name)}"
        )

    def handle_all(_: list[str]) -> None:
        for contact_name, contact_phone_number in contacts.items():
            print(f"{contact_name} - {contact_phone_number}")

    handlers: dict[str, callable] = {
        "hello": handle_hello,
        "add": handle_add,
        "change": handle_change,
        "phone": handle_phone,
        "all": handle_all,
    }

    while True:
        try:
            user_input = input("Enter a command: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            break

        if not user_input.strip():
            continue

        command, args = parse_input(user_input)
        command = command.lower()

        if command in ("exit", "close"):
            print("Good bye!")
            break

        handler = handlers.get(command)
        if handler is None:
            print("Invalid command")
            continue

        handler(args)

if __name__ == "__main__":
    main()