import base64

while True:

    print("\n=== Base64 Encoder/Decoder ===")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":

        text = input("Enter text: ")

        encoded = base64.b64encode(text.encode()).decode()

        print("\nEncoded Text:")
        print(encoded)

    elif choice == "2":

        text = input("Enter Base64 text: ")

        try:
            decoded = base64.b64decode(text.encode()).decode()

            print("\nDecoded Text:")
            print(decoded)

        except:
            print("\nInvalid Base64 input!")

    elif choice == "3":

        print("Goodbye!")
        break

    else:
        print("\nInvalid choice!")