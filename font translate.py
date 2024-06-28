def translate_to_square_chars(input_string):
    char_map = {
        'A': 'Λ', 'B': 'Β', 'C': '⊂', 'D': 'ԁ', 'E': 'Ξ', 'F': 'Ғ', 
        'G': 'Ԍ', 'H': 'Н', 'I': 'Ӏ', 'J': 'Ј', 'K': 'Κ', 'L': '⅃', 
        'M': 'М', 'N': 'И', 'O': 'Θ', 'P': 'Ρ', 'Q': 'Ԛ', 'R': 'Γ', 
        'S': 'Ѕ', 'T': 'Т', 'U': 'Ц', 'V': 'Ѵ', 'W': 'Ш', 'X': 'Χ', 
        'Y': 'Ү', 'Z': 'Ζ', 'a': 'Λ', 'b': 'Ь', 'c': '⊂', 'd': 'ԁ', 
        'e': 'Ξ', 'f': 'ғ', 'g': 'Ԍ', 'h': 'һ', 'i': 'і', 'j': 'ј', 
        'k': 'κ', 'l': 'ⅼ', 'm': 'м', 'n': 'и', 'o': 'Θ', 'p': 'ρ', 
        'q': 'ԛ', 'r': 'г', 's': 'ѕ', 't': 'т', 'u': 'ц', 'v': 'ѵ', 
        'w': 'ш', 'x': 'χ', 'y': 'у', 'z': 'ᴢ'
    }

    translated_string = ''.join(char_map.get(char, char) for char in input_string)
    return translated_string

while True:
    input_string = input("Enter a string to translate: ")
    if input_string == 'EXIT...':
        break
    translated_string = translate_to_square_chars(input_string)
    print("Translated string:", translated_string)