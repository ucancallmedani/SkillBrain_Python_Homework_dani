# Exercitiu 1
numar_1, numar_2 = map(float, input("\n\nScrie doua numere separate prin spatiu: " ).split())
print("\nNumerele dvs sunt: ", numar_1, ",", numar_2)
print("\nAdunare: ", numar_1 + numar_2)
print("\nScadere: ", numar_1 - numar_2)
print("\nInmultire: ", numar_1 * numar_2)
print("\nImpartire: ", numar_1 / numar_2 )
print("\nImpartire intreaga: ", numar_1 // numar_2)
print("\nRestul impartirii: ", numar_1 % numar_2)
print("\n")


# Exercitiu 2

lungime, latime = map(float, input("Scrie doua valori pentru lungime si latime: ").split())
print("\nLungimea este ",lungime," si latimea este ",latime)
print("\nPerimetrul este ", 2 * (lungime + latime))
print("\nAria este ", lungime * latime)
print("\n")


# Exercitiu 3

numar1, numar2 = map(float, input("Scrie doua numere pentru a fi comparate: ").split())
print("\nNumerele dvs sunt: ", numar1, ",", numar2)
print("\nNumarul", numar1, "este mai mare decat", numar2 , numar1 > numar2)
print("\nNumarul", numar1, "este mai mic decat", numar2 , numar1 < numar2)
print("\nNumarul", numar1, "este egal cu", numar2 , numar1 == numar2)
print("\n")


# Exercitiu 4

numar_input = int(input("Scrie un numar intreg: "))
print(str(numar_input) + " este " + ["par", "impar"][numar_input % 2])
print("\n")


# Exercitiu 5

an_nastere = int(input("In ce an v-ati nascut? "))
an_curent = 2025
print("Dvs aveti", an_curent - an_nastere, "ani." )
print("\n")


# Exercitiu 6

secunde_totale = int(input("Scrie un numar de secunde: "))
numar_ore = secunde_totale // 3600
secunde_ramase = secunde_totale % 3600
minute = secunde_ramase // 60
secunde = secunde_ramase % 60
print(numar_ore, "ore,",  minute, "minute,", secunde, "secunde")
print("\n\n")