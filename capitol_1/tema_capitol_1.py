# Tema: Capitolul 1 

# Într-un fișier Python numit tema_capitol_1.py, scrieți un program care să conțină 4 variabile cu valori introduse de utilizator folosind funcția input(). 
# În funcția input() trebuie scrise întrebări adresate utilizatorului, pe care să le ajustați astfel încât răspunsurile să corespundă tipurilor variabilelor: 
# una de tip str (text), una convertită cu int(), una cu float() și una cu bool(). 
# Programul va afișa apoi fiecare variabilă împreună cu tipul acesteia, folosind funcțiile print() și type().

print("\nBuna!")
brand_masina = str(input("\n\nCe fel de masina aveti?: "))
print("\nDvs aveti o masina de brand "+ brand_masina)
print(type(brand_masina))

cai_putere = int(input("\n\nCati cai putere are masina dvs?: "))
print("\nMasina dvs are "+str(cai_putere)+" cai putere")
print(type(cai_putere))

latime_masina = float(input("\n\nCe latime are masina dvs?: "))
print("\nMasina dvs are "+str(latime_masina)+" m")
print(type(latime_masina))

raspuns = bool(input("\n\nSunteti multumit de masina dvs? (Da/Nu) "))
print(type(raspuns))
print("\n")

