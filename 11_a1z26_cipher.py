"""
    Link: https://github.com/TheAlgorithms/Python/blob/master/ciphers/a1z26.py

    a1z26 cipher
        mohammadhssn <=> [109, 111, 104, 97, 109, 109, 97, 100, 104, 115, 115, 110]
"""


def encode(plain):
    return [ord(elm) - 96 for elm in plain]


def decode(encode):
    return ''.join(chr(elm + 96) for elm in encode)


print(encode('mohammadhssn'))
print(decode([13, 15, 8, 1, 13, 13, 1, 4, 8, 19, 19, 14]))
