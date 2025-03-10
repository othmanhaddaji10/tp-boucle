n = int(input("Entrez un entier : "))
diviseurs = [i for i in range(1, n + 1) if n % i == 0]
print(f"Les diviseurs de {n} sont : {diviseurs}")