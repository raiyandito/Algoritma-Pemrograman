# Program untuk membaca file berisi bilangan dan mengidentifikasi jenis bilangannya ganjil atau genap lalu menulisnya dalam bentuk tabel, dan mengurutkan bilangannya di sebuah file txt

# Buka dan baca file berisi angka acak tersebut
with open("Tugas Alpro 1.1.2 - random.txt", "r") as file:
    bilangan = [int(line.strip()) for line in file]

# Identifikasi angka termasuk jenis bilangan ganjil atau genap dan hitung jumlah angka tiap jenis bilangan
bilangan_ganjil = [num for num in bilangan if num % 2 != 0]
bilangan_genap = [num for num in bilangan if num % 2 == 0]

# Urutkan daftar
bilangan_ganjil.sort()
bilangan_genap.sort()
bilangan.sort()

# Hitung jumlah
hitungan_ganjil = len(bilangan_ganjil)
hitungan_genap = len(bilangan_genap)

# Tulis hasilnya dalam sebuah file teks baru
with open("Tugas Alpro 1.2.2 - output.txt", "w") as output_file:
    output_file.write("+----------------+--------+\n")
    output_file.write("| Jenis Bilangan | Jumlah |\n")
    output_file.write("+----------------+--------+\n")
    output_file.write(f"| Ganjil         |{hitungan_ganjil:6}  |\n")
    output_file.write(f"| Genap          |{hitungan_genap:6}  |\n")
    output_file.write("+----------------+--------+\n")

    output_file.write("\nUrutan Bilangan: Ganjil\n")
    output_file.write("\n".join(map(str, bilangan_ganjil)) + "\n\n")

    output_file.write("Urutan Bilangan: Genap\n")
    output_file.write("\n".join(map(str, bilangan_genap)) + "\n\n")

    output_file.write("Urutan Bilangan: Keseluruhan\n")
    output_file.write("\n".join(map(str, bilangan)) + "\n")