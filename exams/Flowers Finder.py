from collections import deque

flowers = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil",
    }
vowels = deque(x for x in input().split())
consonants = [x for x in input().split()]
word_found = False

while vowels and consonants:
    if word_found:
        break
    c_vowel = vowels.popleft()
    c_consonant = consonants.pop()

    for key, value in flowers.items():
        if c_vowel in value:
            len_word = len(value)
            checked_word = ""
            for i in range(len_word):
                checked_letter = value[i]
                if c_vowel not in checked_letter:
                    checked_word += checked_letter
            flowers[key] = checked_word
    for key,value in flowers.items():
        if c_consonant in value:
            len_word = len(value)
            checked_word = ''
            for i in range(len_word):
                checked_letter = value[i]
                if c_consonant not in checked_letter:
                    checked_word += checked_letter
            flowers[key] = checked_word
        if len(flowers[key]) == 0:
            word_found = True
            break


if not word_found:
    print("Cannot find any word!")
else:
    for k, v in flowers.items():
        if len(flowers[k]) == 0:
            print(f"Word found: {k}")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")