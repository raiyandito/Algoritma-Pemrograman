#Program untuk membuat 100 angka acak di file txt

import random

# Buat 100 angka acak dalam rentang bilangan 0-399
angka_acak = [random.randint(0, 399) for _ in range(100)]

# Tulis angkanya dalam file teks
with open("Tugas Alpro 1.1.2 - random.txt", "w") as file:
    for number in angka_acak:
        file.write(str(number) + "\n")

# Berlanjut di program "Tugas Alpro 1.2.1.py"