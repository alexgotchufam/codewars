class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self.key = key
        self.len_key = len(key)
        self.alphabet = alphabet
        self.len_alphabet = len(alphabet)


    def encode(self, text: str) -> str:
        result = []
        for i, c in enumerate(text):
            try:
                old_index = self.alphabet.index(c)
            except ValueError:
                result.append(c)
                continue
            
            corresponding_key = self.key[i % self.len_key]
            shift = self.alphabet.index(corresponding_key)
            
            new_index = (old_index + shift) % self.len_alphabet
            result.append(self.alphabet[new_index])

        return ''.join(result)

    def decode(self, text: str) -> str:
        result = []
        for i, c in enumerate(text):
            try:
                new_index = self.alphabet.index(c)
            except ValueError:
                result.append(c)
                continue
            
            shift = self.alphabet.index(self.key[i % self.len_key])
            old_index = (new_index - shift + self.len_alphabet) % self.len_alphabet
            result.append(self.alphabet[old_index])
        return ''.join(result)

if __name__ == "__main__":
    abc = "abcdefghijklmnopqrstuvwxyz"
    key = "password"
    cipher = VigenereCipher(key, abc)
    encode_str = cipher.encode('coJKHewars')
    print(encode_str)
    decode_str = cipher.decode(encode_str)
    print(decode_str)
