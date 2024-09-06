'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №3.01
Домашняя работа по уроку "Пространство имён"
'''
# Функция подсчета вызовов остальных функций
def count_calls():
    global calls
    calls += 1


# Функция анализирует строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
def string_info(string:str):
    len_string = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    count_calls()
    return (len_string, upper_string, lower_string)


# Функция анализирует строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует
def  is_contains(string:str, listing:list):
    string = string.lower()
    listing = [s.lower () for s in listing]
    count_calls()
    return string in listing
    

# Установка счетчика вызова функций count_calls() и string_info()
calls =0

# Блок вызовов функций и вывода результатов
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(string_info('Abracadabra'))
print(is_contains('Abracadabra', ['abra', 'cadabra'])) # No matches
print(is_contains('Abracadabra', ['abra', 'abracadabra'])) # Match
print(calls)
