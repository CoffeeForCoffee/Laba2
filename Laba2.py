import re

"""СНИЛС ВИДА XXX-XXX-XXX XX"""

SNILS_REGEX = r"^\d{3}-\d{3}-\d{3} \d{2}$"
filename = 'random_snils.txt'

# Функция проверки СНИЛС
def is_valid_snils(snils):
    """Проверяет, соответствует ли СНИЛС формату."""
    return re.match(SNILS_REGEX, snils) is not None

# Функция поиска СНИЛС в файле
def find_snils_in_file(filename):
    """Ищет все подходящие СНИЛС в файле."""
    snils_list = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip("\n")
            if is_valid_snils(line):
                snils_list.append(line)
    return snils_list

found_snils = find_snils_in_file(filename)
print("Найденные СНИЛС:", found_snils)

# Пользовательский ввод
user_input = input("Введите СНИЛС (формат XXX-XXX-XXX XX): ")
if is_valid_snils(user_input):
    print("Это корректный СНИЛС.")
else:
    print("Это не СНИЛС.")