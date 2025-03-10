mport random

nombre_secret = random.randint(1, 50)
essais = 5

print("J'ai choisi un entier entre 1 et 50. A vous de le deviner en 5 tentatives au maximum !")

for essai in range(1, essais + 1):
    proposition = int(input(f"Essai no {essai} : "))
    if proposition < nombre_secret:
        print("Trop petit")
    elif proposition > nombre_secret:
        print("Trop grand")
    else:
        print(f"Bravo ! Vous avez trouvé {nombre_secret} en {essai} essais")
        break
else:
    print(f"Vous avez perdu. Le nombre était : {nombre_secret}")