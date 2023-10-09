klucz = 14
oddzielacz = ";"
tekst = input("tutaj wpisz klucz: ")
ascitran = ""

for i in tekst:
    x = ord(i)

    x = int(x) * klucz
    ascitran = ascitran + str(x) + oddzielacz

print(ascitran)

