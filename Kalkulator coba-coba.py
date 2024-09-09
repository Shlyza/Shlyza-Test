print("choose the operesyen numbah!!!")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
print("5. Luas Persegi")
print("6. Luas Balok")
print("7. Luas Segitiga")
print("8. Luas Lingkaran")

operasi = input()

if operasi == "1":
  num1 = float(input("Masukkan Angka Pertama: "))
  num2 = float(input("Masukkan Angka Kedua: "))
  result = num1 + num2
  print(num1, "+", num2, "=", (round(result, 3)))

elif operasi == "2":
  num1 = float(input("Masukkan Angka Pertama: "))
  num2 = float(input("Masukkan Angka Kedua: "))
  result = num1 - num2
  print(num1, "-", num2, "=", (round(result, 3)))

  
elif operasi == "3":
  num1 = float(input("Masukkan Angka Pertama: "))
  num2 = float(input("Masukkan Angka Kedua: "))
  result = num1 * num2
  print(num1, "*", num2, "=", (round(result, 3)))
  
elif operasi == "4":
  num1 = float(input("Masukkan Angka Pertama: "))
  num2 = float(input("Masukkan Angka Kedua: "))
  result = num1 / num2
  print(num1, "/", num2, "=", (round(result, 3)))
  
elif operasi == "5":
  num1 = float(input("Masukkan Panjang Sisi: "))
  result = num1 * num1
  print(num1, "*", num1, "=", (round(result, 3)))
  
elif operasi == "6":
  num1 = float(input("Masukkan Panjang: "))
  num2 = float(input("MasukkanLebar: "))
  num3 = float(input("Masukkan Tinggi: "))
  result = num1 * num2 * num3
  print(num1, "*", num2,"*", num3, "=", (round(result, 3)))

elif operasi == "7":
  num1 = float(input("Masukkan Alas: "))
  num2 = float(input("Masukkan Tinggi: "))
  result = (num1 * num2)/2  
  print("(", num1, "*", num2, ")","/ 2", "=", (round(result, 3)))
  
elif operasi == "8":
  print("1. Diketahui Diameter")
  print("2. Diketahui Jari-Jari")
  Opelasi = input()
  if Opelasi == "1":
   num1 = float(input("Masukkan Diameter: "))
   result = (3.14 *  (num1**2))/4
   print("(", "3.14", "*", num1, "^2", ")","/ 4", "=", (round(result, 3)))
  elif Opelasi == "2":
   num1 = float(input("Masukkan Jari-Jari: "))
   result = (22 * (num1**2))/7
   print("(", "22", "(", num1, "^2", ")", ")", "/ 7", "=", (round(result, 3)))
  else:
   print("Salah Teken?")

else:
  print("Salah Teken?")