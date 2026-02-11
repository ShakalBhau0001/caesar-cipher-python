def caesar_cipher(text, shift, direction):
    result = ""

    # Direction handling
    if direction == "L":
        shift = -shift
    elif direction == "R":
        pass
    else:
        return "Invalid direction! Use L or R."

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


print("Caesar Cipher \n")

message = input("Enter message: ")
shift = int(input("Enter shift key: "))
direction = input("Choose direction (L = Left, R = Right): ").upper()

encrypted = caesar_cipher(message, shift, direction)
print("\nEncrypted Message:", encrypted)

# Decryption uses opposite direction
opposite = "L" if direction == "R" else "R"
decrypted = caesar_cipher(encrypted, shift, opposite)

print("Decrypted Message:", decrypted)
