import base64
from colorama import init, Fore

# Initialize colorama
init()

while True:

    print(Fore.CYAN + "\n=== Base64 Encoder/Decoder ===")
    print(Fore.YELLOW + "1. Encode")
    print(Fore.YELLOW + "2. Decode")
    print(Fore.YELLOW + "3. Exit")

    choice = input(Fore.WHITE + "Choose option: ")

    if choice == "1":

        text = input(Fore.WHITE + "Enter text: ")

        encoded = base64.b64encode(text.encode()).decode()

        print(Fore.GREEN + "\nEncoded Text:")
        print(Fore.GREEN + encoded)

    elif choice == "2":

        text = input(Fore.WHITE + "Enter Base64 text: ")

        try:
            decoded = base64.b64decode(text.encode()).decode()

            print(Fore.GREEN + "\nDecoded Text:")
            print(Fore.GREEN + decoded)

        except:
            print(Fore.RED + "\nInvalid Base64 input!")

    elif choice == "3":

        print(Fore.CYAN + "Goodbye!")
        break

    else:
        print(Fore.RED + "\nInvalid choice!")