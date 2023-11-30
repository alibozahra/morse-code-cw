# Define the Morse code dictionary
morse_code_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    ' ': ' '
}

# Define the reverse Morse code dictionary (English to Morse code)
reverse_morse_code_dict = dict(zip(morse_code_dict.values(), morse_code_dict.keys()))

def morse_code(phrase, option):
    # Initialize the encoded or decrypted phrase
    encoded_phrase = ""

    # Encrypt the phrase
    if option == "e":
         # Convert the phrase to lowercase and remove spaces
        phrase = phrase.lower().replace(" ", "")
        for char in phrase:
            if char in morse_code_dict:
                encoded_phrase += morse_code_dict[char] + " "
            else:
                print("Invalid character:", char , ",please use alphabets")
                return

        # Return the encoded phrase
        return encoded_phrase

    # Decrypt the phrase
    elif option == "d":
        for morse_code in phrase.split(" "):
            if morse_code in reverse_morse_code_dict:
                encoded_phrase += reverse_morse_code_dict[morse_code]
            else:
                print("Invalid Morse code:", morse_code)
                return

        # Return the decrypted phrase
        return encoded_phrase

    # Invalid option
    else:
        print("Invalid option. Please choose either e (encrypt) or d (decrypt).")

# Get the phrase to encrypt or decrypt from the user
phrase = input("Enter the phrase to encrypt or decrypt: ")

# Determine whether to encrypt or decrypt
option = input("Encrypt (e) or decrypt (d): ")

# Encrypt or decrypt the phrase
encoded_phrase = morse_code(phrase, option)

# Print the encoded or decrypted phrase
print("Encrypted phrase:" if option == "e" else "Decrypted phrase:", encoded_phrase)