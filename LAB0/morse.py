import sys


morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..'
}


def read_from_txt(file_name):
    with open(file_name, 'r') as file:
        data = []
        for line in file:
            data.append(line.upper().strip())
    return data


def morse_translation(sentance: str):
    result = ''
    for letter in sentance:
        if letter == ' ':
            result += '/ '
        try:
            result += (morse_code_dict[letter] + ' ')
        except KeyError:
            pass
    return result


def main():
    file_name = sys.argv[1]
    print(file_name)
    data = read_from_txt(file_name)
    for line in data:
        print(morse_translation(line))


main()
