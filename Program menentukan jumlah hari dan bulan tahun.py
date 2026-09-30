Program menentukan jumlah hari dalam bulan tertentu dengan while

bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

while bulan < 1 or bulan > 12:
    print("Bulan tidak valid, harus 1-12.")
    bulan = int(input("Masukkan bulan (1-12): "))

if bulan in [1, 3, 5, 7, 8, 10, 12]:
    hari = 31
elif bulan in [4, 6, 9, 11]:
    hari = 30
else:  # bulan == 2
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        hari = 29
    else:
        hari = 28

print(f"Jumlah hari pada bulan {bulan} tahun {tahun} adalah {hari}.")
