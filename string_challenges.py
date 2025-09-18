# Вывести последнюю букву в слове
word = 'Архангельск'

print(word[10:11])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count("а"))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
vowel_count = sum(1 for char in word if char in vowels)
print(f"Количество гласных в слове '{word}': {vowel_count}")


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
word_count = len(sentence.split())
print(f"Количество слов в предложении: {word_count}")

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
word = sentence.split()#[Мы приехали в гости]
for i in word:
    print(i[0])













# Вывести усреднённую длину слова в предложении


sentence = 'Мы приехали в гости'

words = sentence.split()

total_length = sum(len(word) for word in words)

average_length = total_length / len(words) if words else 0

print(f"Средняя длина слова: {average_length:.2f}")