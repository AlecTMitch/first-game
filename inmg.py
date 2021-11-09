
def rotate_letter(input):
    sequence = "abcdefghijklmnopqrstuvwxyz"
    alphabet = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
        "i": 8,
        "j": 9,
        "k": 10,
        "l": 11,
        "m": 12,
        "n": 13,
        "o": 14,
        "p": 15,
        "q": 16,
        "r": 17,
        "s": 18,
        "t": 19,
        "u": 20,
        "v": 21,
        "w": 22,
        "x": 23,
        "y": 24,
        "z": 25
    }
    if input == " ":
        return " "
    index = (alphabet[input] + 13) % 26
    return sequence[index]


def rot13(input):
    output = ""
    for letter in input:
         output = output + rotate_letter(letter)
    return output

print(rot13("v ybir lbh ferl"))

