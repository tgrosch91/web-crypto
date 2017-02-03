alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encrypt(text,rot):
    global alphabet
    new_text = ""
    for letter in text:
        new_letter = rotate_character(letter, rot)
        new_text += new_letter
    return new_text

def alphabet_position(letter):
    global alphabet
    letter = letter.lower()
    position = alphabet.index(letter)
    return position


def rotate_character(char,rot):
    global alphabet
    if char.lower() == char and char in alphabet:
        current_pos = alphabet_position(char)
        new_pos = (current_pos + rot)%len(alphabet)
        new_char = alphabet[new_pos]
        return new_char
    elif char.lower() in alphabet:
        current_pos = alphabet_position(char.lower())
        new_pos = (current_pos + rot)%len(alphabet)
        new_char = alphabet[new_pos]
        new_char = new_char.upper()
        return new_char
    else:
        return char
