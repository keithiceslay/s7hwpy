# Задача 34

vowels = ('а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е')
poem = str(input('Введите стих\n')).lower().split()
vowel_count = list()
check = lambda x, y: x == y
for i in range(len(poem)):
    count = 0
    for j in range(len(poem[i])):
        if poem[i][j] in vowels: 
            count += 1
    vowel_count.append(count)
for i in range(len(vowel_count)-1): 
    if not check(vowel_count[i], vowel_count[i+1]):
        print('Пам парам')
        break
if check(vowel_count[i], vowel_count[i+1]): print('Парам пам-пам')
