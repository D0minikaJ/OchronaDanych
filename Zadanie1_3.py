from collections import Counter


def caesar_decrypt(message, shift):
    result = ""
    for char in message.upper():
        if char.isalpha():  # if char is alphabet
            char_code = ord(char) - shift
            if char_code < 65:  # first ascii
                char_code += 26  # range of alphabet
            result += chr(char_code)
        else:
            result += char
    return result


def frequency_analysis(message):
    letter_count = Counter()  # frequency of each letter
    for char in message.upper():
        if char.isalpha():
            letter_count[char] += 1
    return letter_count


def break_caesar_cipher(ciphertext, top_n=5):
    letter_frequencies = frequency_analysis(ciphertext)
    most_common_letter = max(letter_frequencies, key=letter_frequencies.get)

    highest_count = 0
    for letter, count in letter_frequencies.items():
        if count > highest_count:
            most_common_letter = letter
            highest_count = count

    # all possible shifts and their decrypted messages
    probable_shifts = []
    for i in range(26):
        shift = (ord(most_common_letter) - ord('A') - i) % 26
        decrypted_text = caesar_decrypt(ciphertext, shift)
        probable_shifts.append((shift, decrypted_text))

    # sort the shifts
    sort_shifts(probable_shifts)

    count = 0
    for shift, decrypted_text in probable_shifts:
        if count < top_n:
            print(f"Shift: {shift}, Decrypted text: {decrypted_text[:100]}...")  # Displaying the first 100 characters
            count += 1


ciphertext = input("Message: ")
top_n = int(input("Combination (1-10): "))

break_caesar_cipher(ciphertext, top_n)
