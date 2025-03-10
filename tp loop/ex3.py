N = int(input("Entrez le nombre d'étudiants : "))
notes = [float(input(f"Entrez la note de l'étudiant {i + 1} : ")) for i in range(N)]
moyenne = sum(notes) / N
print(f"La moyenne de la classe est : {moyenne:.2f}")