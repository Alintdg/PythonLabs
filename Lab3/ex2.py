def count_letters(text):
    result = {}
    for letter in text:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

print(count_letters("Helllloooooo"))