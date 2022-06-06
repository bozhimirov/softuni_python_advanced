def words_sorting(*args):
    word_dict = {}
    for arg in args:
        word_dict[arg] = 0
        sum_ord = 0
        for letter in range(len(arg)):
            value_letter = ord(arg[letter])
            sum_ord += value_letter
        word_dict[arg] = sum_ord
    sum_dict = 0
    for words in word_dict:
        sum_dict += word_dict[words]
    if sum_dict % 2 == 0:
        sorted_words = sorted(word_dict.items(), key=lambda x: x[0])
    else:
        sorted_words = sorted(word_dict.items(), key=lambda x: -x[1])

    result = []
    for key, value in sorted_words:
        result.append(f'{key} - {value}')
    return '\n'.join(result)