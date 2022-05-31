import itertools
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Иван', 'Оксана']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
result = (out for out in itertools.zip_longest(tutors, klasses, fillvalue=None))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
