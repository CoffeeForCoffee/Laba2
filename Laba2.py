import re
import unittest

"""СНИЛС ВИДА XXX-XXX-XXX XX"""

with open("random_snils.txt", "w", encoding="utf-8") as file:
    file.write("""123-456-789 01
987-654-321 99
000-000-000 00
123-456-78 90
456-123-78910
abc-def-ghi jk
123-456-789-01
32165498700
999-888-777 11
111-222-333 44
""")
print("Файл random_snils.txt успешно создан.")