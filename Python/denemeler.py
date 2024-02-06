def faktoriyel(sayi):
  if sayi == 0 or sayi == 1:
    return 1
  else:
    return sayi * faktoriyel(sayi - 1)

sayi = int(input("Lütfen bir sayı giriniz: "))

sonuc = faktoriyel(sayi)

print(sonuc)
