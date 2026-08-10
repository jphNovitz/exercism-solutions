"""Implement a rotational cipher using a given key."""


def rotate(text, key):
    """Rotate each letter in the text by the given key."""
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    size_alpha = len(alphabet)
    limit = len(alphabet) - key

    for car in text:
        if car not in alphabet:
            if car.isupper():
                car = car.lower()
                pos = alphabet.index(car)
                if pos <= limit:
                    new_pos = pos + key
                    if new_pos >= size_alpha:
                        new_pos = new_pos - size_alpha
                    result += alphabet[new_pos].upper()
                else:
                    new_pos = pos + key
                    if new_pos < size_alpha:
                        result += alphabet[new_pos]
                    else:
                        new_pos = abs(size_alpha - new_pos)
                    result += alphabet[new_pos].upper()
            else:
                result += car
        else:
            pos = alphabet.index(car)
            new_pos = pos + key
            if new_pos >= size_alpha:
                new_pos = abs(new_pos - size_alpha)
            result += alphabet[new_pos]

    return result
