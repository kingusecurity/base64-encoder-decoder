import base64

print("=== Base64 Encoder/Decoder ===")

choice = input("Encode or Decode? (e/d): ")

if choice == "e":
    text = input("Enter text: ")

    encoded = base64.b64encode(text.encode()).decode()

    print("Encoded:", encoded)

elif choice == "d":
    text = input("Enter Base64 text: ")

    decoded = base64.b64decode(text.encode()).decode()

    print("Decoded:", decoded)

else:
    print("Invalid option")