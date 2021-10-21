"""
    Link: https://github.com/TheAlgorithms/Python/blob/master/ciphers/onepad_cipher.py
"""

import random


class OneTime:
    def encrypt(self, text):
        plain = [ord(i) for i in text]
        cipher = []
        key = []

        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        return cipher, key

    def decrypt(self, cipher, key):
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))
        return ''.join(plain)


c, k = OneTime().encrypt('mohammadhssn')
print(c)
print(k)

print(OneTime().decrypt(c, k))