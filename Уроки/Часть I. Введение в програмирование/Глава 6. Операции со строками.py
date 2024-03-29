print("Операции со строками".upper())
# Операции со строками.
#=================================================================================================================================
# Тройные строки
# Если строка занимает более одной строки кода, нужно поместить эту строку в тройные кавычки:
print(
"""строка один
строка два
строка три""")
#_________________________________________________________________________________________________________________________________
# Индексы
# Строки итерируемы (как списки и кортежи) - программа может их перебирать значение за знаечением, то есть
# к каждому элементу можно получить доступ через цикл. Первый элемент начинается с 0 индекса.

print("Кафка"[0]) # Без переменной тоже можно
author = "Кафка"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])
# Если попытаться извлечь символ, символ которого больше, чем индукс строки, Python сгенерирует исключение IndexError.

# Также можно извлекать элементы из списка с помощью отрицательного индекса.
# Чтобы получить доступ к последнему элементу в итерируемом объекте, можно использовать отрицательные индекс -1
print(author[-1]) # 'а'
print(author[-2]) # 'к'
print(author[-3]) # 'ф'

#_________________________________________________________________________________________________________________________________
# Строки неизменяемы
# Как и кортежи, строки неизменяемы. Нельзя изменить символы в строке - если нужно это сделать, создайте новую строку.
ff = "Ф. Фицджеральд"
ff = "Ф. Скотт Фицджкральд"
print(ff)

#_________________________________________________________________________________________________________________________________
# Конкатенация
# Конкатенация - соединение строк. Пример:
print("кот" + "в" + "шляпе")
print("кот " + "в " + "шляпе")

#_________________________________________________________________________________________________________________________________
# Умножение строк
# С помощью оператора умножения строку можно умножать на число.
print("о" * 4 + " либераху порвало")

#_________________________________________________________________________________________________________________________________
# Изменение регистра
# При помощи метода upper() можно превратить каждую букву в строке в прописну.
print("Истина где-то радом...".upper())

# Аналогично каждую букву в строке можно сделать строчной, вызвав в этой строке метод lower().
print("ТАК БУДЕТ ПРОДОЛЖАТЬСЯ.".lower())

# Первую букву предложения можно сделать прописной, вызвав метод capitalize().
print("троглодиты...".capitalize())

#_________________________________________________________________________________________________________________________________
# Метод format
# Новую строку можно создаь при помощи метода format(), проверяющего вхождения в строке фигурных скобок {} и заменяющего их
# переданными ему параметрами.
print("Уильям {}".format("Фолкнер"))

# В качестве пораметра можно также передавать переменную
last = "Фолкнер"
print("Уильям {}".format(last))

# В строке можно использовать неограниченное количество фигурных скобок
author = "Уильям Фолкнер"
year_born = "1897"
print("{} родился в {}.".format(author, year_born))

# Метод format() может пригодитсья, если вы создаёте строку из пользовательского ввода.
n1 = input("Введите существительное: ")
v = input("Введите глагол: ")
adj = input("Введите прилагательное: ")

r = """Как обычно, {} {} {} {}
    """.format(n1, v, adj, input("Введите существительное: "))
print(r) # можно без переменной

#_________________________________________________________________________________________________________________________________
# Метод split
# Метод split() используется для разделения одной строки на две или более строк.
print("Я прыгнул через голову. Это целых 2 метра!".split(".")) # Результат: строка до точки и строка после точки.
# В результате получился список с двумя элементами

#_________________________________________________________________________________________________________________________________
# Метод join
# Метод join() позволяет добавлять новые символы между всеми символами в строке.
first_three = "абв"
result = "+".join(first_three)
print(result)# можно без переменной

# Превратить список строк в единую строку можно, вызвав метод join() в пустой строке
# и передав этот список в качестве параметра метода.
words = ["Рыжая",
         "лисица",
         "сделала",
         "кувырок",
         "через",
         "голову",
         "."]
one = " ".join(words)
print(one) # можно без переменной

#_________________________________________________________________________________________________________________________________
# Метод strip
# Метод strip() используется для удаления пробельных символов в начале и конце строки.
s = "    ХХХХХаХХХХХ    "
print(s.strip()) # можно без переменной

#_________________________________________________________________________________________________________________________________
# Метод replace
# Метод replace() заменяет каждое вхождение строки другой строкой.
# Первый параметр - строка, которую нужно заменить, второй - строка, которой нужно заменить вхождения.
print("Все животные одинаковые...".replace("о", "@"))

#_________________________________________________________________________________________________________________________________
# Поиск индекса
# Индекс первого вхождения символа в сроке можно найти с помощью метода index()
# Передайте в качестве параметра метода символ, который ищете, и метод index вернёт индекс первого вхождения этого символа в строке.
print("животные".index("н"))
# Если метод index не найдёт соответствия, то Python сгенерирует исключение ValueError.

#_________________________________________________________________________________________________________________________________
# Ключевое слово in
# Ключевое слово in проверяет, содержится ли строка в другой строке, и возвращает значение True или False.
print("Кот" in "Кот в шляпе.")
print("Мышь" not in "Кот в шляпе.") # Проверка отсутствие строки в другой строке

#_________________________________________________________________________________________________________________________________
# Управляющие символы
# Чтобы не получить синтаксическую ошибку внутри строки при вводе кавычек,
# можно поместить перед кавычками символ обратного слеша.
print("Она сказала: \"Непременно\"") ## Проще поместить двойные кавычки в одинарные.
# Управляющие символы Python сообщают, что знак, перед которым они помещены, не имеет специально значения,
# а предназначен для представления обычного символа.

#_________________________________________________________________________________________________________________________________
# Новая строка
# Помещение символов \n внутрь строки выполняет перенос строки.
print("строка1\nстрока2\nстрока3")

#_________________________________________________________________________________________________________________________________
# Извлечение среза
# Извлечение среза - это способ вернуть новый итерируемый объект, состоящий из подмножества элементов другого итерируемого объекта.
fict = ["Толстой",
        "Дик",
        "Оруэлл",
        "Пелевин",
        "Остин"]
print(fict[0:3]) # 0 - начало среза, 3 - конец среза "ДО"
# Пример извлечения среза строки:
ivan = """Пётр Иванович успокоился и с интересом стал
расспрашивать подробности о кончика Ивана Ильича."""

print(ivan[0:24])   # Если начальный индекс - 0, тогда можно оставить его пустым: ivan[:24]
print(ivan[25:93])    # Если конечный индекс последний в итерируемом объекте, можно оставить его пустым: ivan[25:]
# Если оставить пустым и начальный, и конечный индексы, то после извлечени среза получить исходный объект.
# Если в строке, к примеру, 5 элементов, то, чтобы указать срез индекса всех, нужно написать [0:5], а не [0:4]




















