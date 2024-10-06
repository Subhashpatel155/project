import random
import os
import sys
from collections import Counter

print("Only alphanumeric characters and spaces can be used!")

# Define the character set for encryption
letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
    "u", "v", "w", "x", "y", "z", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "0", "1", "2", "3", "4", "5", "6", 
    "7", "8", "9", " "
]

def get_custom_shift():
    while True:
        try:
            shift = int(input("Enter a custom shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Please enter a value between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content saved to {filename}")

def load_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content loaded from {filename}")
        return content
    else:
        print(f"{filename} does not exist.")
        return None

def analyze_frequency(message):
    counter = Counter(message)
    print("\nCharacter Frequency Analysis:")
    for char, freq in counter.items():
        print(f"'{char}': {freq}")

def Encryption(message, shift):
    codelist = []
    for i in message:
        if i not in letters:
            continue  # Skip characters not in the letters list
        encl0 = str(letters.index(i) + shift)
        encl1 = str(letters.index(i) + shift - 26) if letters.index(i) + shift - 26 >= 0 else encl0
        encl2 = str(letters.index(" ") + random.randint(19, 36))  # Random shift for space
        
        if letters.index(i) < 52:  # Alphabetic characters
            if i.isupper():
                encl1 += "x"
                codelist.append(encl1)
            else:
                encl0 += "f"
                codelist.append(encl0)
        elif letters.index(i) == 62:  # Space character
            encl2 += "f" if random.randint(1, 2) == 1 else "x"
            codelist.append(encl2)
        else:  # Numeric characters
            if int(letters.index(i)) % 2 == 0:
                encl0 += "y"
                codelist.append(encl0)
            else:
                encl0 += "a"
                codelist.append(encl0)

    return ''.join(codelist)  # Join list to form the encrypted string

def Decryption(messagecode, shift): 
    slicedcode = [messagecode[i:i + 3] for i in range(0, len(messagecode), 3)]
    indx = []
    
    for item in slicedcode:
        if len(item) < 3:
            continue  # Skip if the item is not complete
        q = int(item[:-1])  # Get the numeric part
        if q > 80:
            indx.append(62)  # Space character
        elif item[-1] == "x":
            indx.append(q + 26 - shift)
        else:
            indx.append(q - shift)

    # Construct the decrypted message from index list
    crackedcode = ''.join(letters[m] for m in indx)
    return crackedcode

def main():
    while True:
        print("\n--- Encryption/Decryption Tool ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Save encrypted message to file")
        print("4. Load message from file and decrypt")
        print("5. Analyze frequency of encrypted message")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            shift = get_custom_shift()
            input_message = input("Input your message: ").strip()
            message = ''.join(filter(lambda x: x in letters, input_message))
            encrypted_message = Encryption(message, shift)
            print("Encrypted message:", encrypted_message)
        
        elif choice == '2':
            shift = get_custom_shift()
            input_encrypted_code = input("Input encrypted code: ").strip()
            messagecode = ''.join(filter(lambda x: x in letters or x.isdigit(), input_encrypted_code))
            decrypted_message = Decryption(messagecode, shift)
            print("Decrypted message:", decrypted_message)

        elif choice == '3':
            shift = get_custom_shift()
            input_message = input("Input your message: ").strip()
            message = ''.join(filter(lambda x: x in letters, input_message))
            encrypted_message = Encryption(message, shift)
            filename = input("Enter filename to save the encrypted message: ")
            save_to_file(filename, encrypted_message)

        elif choice == '4':
            filename = input("Enter filename to load the encrypted message: ")
            loaded_message = load_from_file(filename)
            if loaded_message:
                shift = get_custom_shift()
                decrypted_message = Decryption(loaded_message, shift)
                print("Decrypted message:", decrypted_message)

        elif choice == '5':
            input_encrypted_code = input("Input encrypted code: ").strip()
            messagecode = ''.join(filter(lambda x: x in letters or x.isdigit(), input_encrypted_code))
            analyze_frequency(messagecode)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
