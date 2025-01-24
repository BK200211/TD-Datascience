# Données de base
X = [1, 2, 3, 4, 5]
Y = [50, 55, 60, 65, 70]

# Régression linéaire
n = len(X)
mean_x = sum(X) / n
mean_y = sum(Y) / n

# Calcul des coefficients
numerator = sum((X[i] - mean_x) * (Y[i] - mean_y) for i in range(n))
denominator = sum((X[i] - mean_x) ** 2 for i in range(n))
slope = numerator / denominator
intercept = mean_y - slope * mean_x

# Score pour la relqtion entre nombre d'heures de revisions et la note finale
x_new = 6
y_pred = slope * x_new + intercept

print("Vous trouverez ci-joint le score de l'étudiant qui a révisé", x_new, "heures" " est de", y_pred)
