# Determina anotimpul folosind luna introdusa de utilizator.


iarna = list(map(str.lower, ["Ianuarie", "Februarie", "Decembrie"]))
primavara = list(map(str.lower ,["Martie", "Aprilie", "Mai"]))
vara = list(map(str.lower, ["Iunie", "Iulie", "August"]))    
toamna = list(map(str.lower, ["Septembrie", "Octombrie", "Noiembrie"]))


luna_utilizator = input("\n\nIn ce luna esti? ").strip().lower()


if luna_utilizator in iarna:
    print("\nEsti in anotimpul Iarna!", "\n\n")

elif luna_utilizator in primavara:
    print("\nEsti in anotimpul Primavara!", "\n\n")

elif luna_utilizator in toamna:
    print("\nEsti in anotimpul Toamna!", "\n\n")

elif luna_utilizator in vara:
    print("\nEsti in anotimpul Vara!", "\n\n")

else:
    print("\nNu am recunoscut luna introdusa.\n\n")