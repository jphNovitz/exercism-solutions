"""Implement a rotational cipher using a given key."""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)


def rotate(text, key):
    """Rotate each letter in the text by the given key."""
    result = ""

    for char in text:
        if char not in ALPHABET:
            if char.isupper():
                pos = ALPHABET.index(char.lower())
                result += get_rotated_character(pos, key, True)
            else:
                result += char
        else:
            pos = ALPHABET.index(char)
            result += get_rotated_character(pos, key, False)

    return result


def get_rotated_character(pos, key, is_upper):
    """Return the character rotated by the given key."""
    new_pos = pos + key
    if new_pos >= ALPHABET_SIZE:
        new_pos = new_pos - ALPHABET_SIZE

    if is_upper:
        return ALPHABET[new_pos].upper()
    return ALPHABET[new_pos]
