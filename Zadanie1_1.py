def caesar(message, shift):
    result = ""

    for char in message.upper():
        if char.isalpha():  # if char is alphabet
            char_code = ord(char)  # change char to ascii
            new_char_code = char_code + shift

            if new_char_code > 90:  # last ascii
                new_char_code -= 26  # range of alphabet

            if new_char_code < 65:  # first ascii
                new_char_code += 26  # range of alphabet

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char

    return result


user_message = input("Message:")
user_shift = int(input("Shift: "))
print(caesar(user_message, user_shift))
