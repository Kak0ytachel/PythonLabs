def solve():
    text = input().lower()
    vowel = ('а', 'я', 'о', 'ё', 'э', 'е', 'у', 'ю', 'ы', 'и')
    consonant = ('й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'в',
                 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'ь', 'б')
    vowels_list = ""
    vowel_counter = 0
    consonant_counter = 0
    replaced_text = ""
    for letter_index in range(0, len(text)):
        letter = text[letter_index]
        if letter in vowel:
            vowel_counter += 1
            vowels_list += letter
        elif letter in consonant:
            consonant_counter += 1
        else:
            replaced_text += ' '
            continue
        replaced_text += letter
    print("Количество гласных:", vowel_counter)
    print("Количество согласных:", consonant_counter)
    if vowel_counter == consonant_counter:
        print("Согласные:", ', '.join(vowels_list))
    print("Количество слов:", sum([int(len(i) != 0) for i in replaced_text.split(sep=' ')]))


if __name__ == '__main__':
    solve()
