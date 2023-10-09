# klucz = 14
# #kod = input("podaj zakodowany ciąg cyfr: ")

# asciint = int(1513359373513359401555596)
# ascistr = str(1513359373513359401555596)

# asciint_exact = int(asciint / klucz)
# asciint_exact_str = str(asciint_exact)
# for i in range (0, len(asciint_exact_str), 3):
#     kod = asciint_exact_str[i:i+3]
#     kod_int = int(kod)
#     #haslo = chr(kod_int)
#     print(kod_int)
    
klucz = 14

# Pobierz zaszyfrowane hasło od użytkownika
zaszyfrowane_haslo = input("Podaj zaszyfrowane hasło: ")
odszyfrowana_wiadomosc = ""
# Zamień zaszyfrowane hasło z powrotem na ciąg znaków ASCII
#dlugosc = len(zaszyfrowane_haslo)
#twoj_kod = "1400;1610;1358;1610;1610;"

litera = 0

litera = zaszyfrowane_haslo.split(";")
litera.pop(-1)


for i in litera:

    wynik = (int(int(i)/klucz))
    odszyfrowana_wiadomosc = odszyfrowana_wiadomosc + str(chr(wynik))
print(odszyfrowana_wiadomosc)
# for litera in range(0,len(litera)-1):
#     print()

# for i in litera:
#     i = int(i)
#     print(i/14)

