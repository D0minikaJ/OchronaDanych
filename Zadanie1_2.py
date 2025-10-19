def vigenere(message, keyword):
    result = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    keyword_index = 0

    for char in message.upper():
        if char.isalpha():  # if char is alphabet
            shift = ord(keyword[keyword_index]) - 65  # current letter in keyword
            char_code = ord(char)  # change char to ascii
            new_char_code = char_code + shift

            if new_char_code > 90:  # last ascii
                new_char_code -= 26  # range of alphabet

            new_char = chr(new_char_code)
            result += new_char

            keyword_index = (keyword_index + 1) % keyword_length    # get a new index
        else:
            result += char

    return result


user_message = input("Message: ")
user_keyword = input("Keyword: ")
print(vigenere(user_message, user_keyword))
