# Tema 4
# Scrie un program care:
# Cere utilizatorului să introducă un PIN.
# Transformă parola în litere mici (lower()).
# Evaluează parola astfel:
# Parolă slabă: dacă are mai puțin de 6 caractere.
# Parolă medie: dacă are 6-10 caractere.
# Parolă sigură: dacă are mai mult de 10 caractere.
# Afișează mesajul corespunzător: „Parolă slabă”, „Parolă medie” sau „Parolă sigură”.


user_password = input("\n\nBuna! Introdu o parola: ").lower()

length = len(user_password)

if length < 6:
    print("\nParola slaba! (prea scurta)")

elif 6 <= length <= 10:
    print("\nParola medie!")

else:
    print("\nParola sigura!")

print("\n")