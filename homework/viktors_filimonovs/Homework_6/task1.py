text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

words = []
curr_word = ""

for character in text:
    if character.isalpha():
        curr_word += character
    else:
        if curr_word:
            words.append(curr_word + "ing")
            curr_word = ""
        words.append(character)
if curr_word:
    words.append(curr_word + "ing")
print(' '.join(words))
