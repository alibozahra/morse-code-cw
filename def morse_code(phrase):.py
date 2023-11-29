def morse_code(phrase):
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

    # Convert the phrase to lowercase and remove spaces
    phrase = phrase.lower().replace(" ", "")

    # Initialize the encrypted or decrypted phrase
    encoded_phrase = ""

    # Iterate through each character in the phrase
    for char in phrase:
        # Check if the character exists in the Morse code dictionary
        if char in morse_code_dict:
            # Add the corresponding Morse code representation to the encoded phrase
            encoded_phrase += morse_code_dict[char] + " "
        else:
            # If the character is not found, ignore it
            pass

    # Return the encoded or decrypted phrase
    return encoded_phrase

# Get the phrase to encrypt or decrypt from the user
phrase = input("Enter the phrase to encrypt or decrypt: ")

# Determine whether to encrypt or decrypt
option = input("Encrypt (e) or decrypt (d): ")

# Encrypt the phrase
if option == "e":
    encoded_phrase = morse_code(phrase)
    print("Encrypted phrase:", encoded_phrase)
elif option == "d":
    # Decrypt the phrase
    decoded_phrase = morse_code(phrase)
    print("Decrypted phrase:", decoded_phrase)
else:
    # Invalid option
    print("Invalid option. Please choose either e (encrypt) or d (decrypt).")