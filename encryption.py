input_str = input("Input String to be Encrypted: ")
input_key = int(input("Input Negative/Positive Key Number for offset to Right/Left: "))

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
            "s", "t", "u", "v", "w", "x", "y", "z"]

def encryptor(text, key = 25):
    text_encrypt = ""
    for str in text:
        # check if character is a space and appends as is
        if str.isspace():
            text_encrypt += str
        # checks if char is a number and offsets it as needed
        elif str.isnumeric():
            n_index = nums.index(str) - (key % 10)
            text_encrypt += nums[n_index]
        # checks if char is an alphabet
        elif str.isalpha():
            # checks if alphabet is uppercase, swaps case and offsets accordingly
            if str.isupper():
                n_index = alphabets.index(str.lower()) - (key % 26)
                text_encrypt += alphabets[n_index]
            # checks if alphabet is lowercase, swaps case and offsets accordingly
            else:
                n_index = alphabets.index(str) - (key % 26)
                text_encrypt += alphabets[n_index].swapcase()
        # if character is any symbol, appends as is
        else:
            text_encrypt += str

    return text_encrypt

def decryptor(text, key=25):

    text_decrypt = ""
    for str in text:
        if str.isspace():
            text_decrypt += str
        elif str.isnumeric():
            n_index = (nums.index(str) + key) % 10
            text_decrypt += nums[n_index]
        elif str.isalpha():
            if str.isupper():
                index = alphabets.index(str.lower())
                n_index = (index + key) % 26
                text_decrypt += alphabets[n_index]
            else:
                index = alphabets.index(str)
                n_index = (index + key) % 26
                text_decrypt += alphabets[n_index].swapcase()

        else:
            text_decrypt += str
    
    return text_decrypt

text_enc = encryptor(input_str)
print(text_enc)

print()
print()

text_decr = decryptor(text_enc)
print(text_decr)

# some say the world will end in fire, some say in ice, from what I've tasted of desire. I hold with those who favor fire

