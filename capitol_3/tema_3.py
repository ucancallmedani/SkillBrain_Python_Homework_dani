# Tema 3


# Scrie un program care:

# Are deja salvate două informații: numele de utilizator și parola corectă.
# Cere utilizatorului să introducă numele de utilizator și parola de la tastatură.

# Verifică următoarele situații:

# Dacă numele de utilizator introdus este corect și parola introdusă este corectă → afișează "Acces permis".
# Dacă doar una dintre cele două este corectă (numele de utilizator sau parola) → afișează "User/Password incorect".
# Dacă ambele sunt greșite → afișează "Acces respins".

username_salvat = input("\nAlege un nume de utilizator: ")
parola_salvata  = input("Alege o parola: ")

print("\nCont creat! Acum trebuie sa te loghezi.")

username_input = input("\nIntrodu numele de utilizator: ")
parola_input   = input("Introdu parola: ")

if username_salvat == username_input and parola_salvata == parola_input:
    print("\nAcces permis.")
elif username_salvat == username_input or parola_salvata == parola_input:
    print("\nUser/Password incorect.")
else:
    print("\nAcces respins.")
print("\n")