from sklearn.neighbors import KNeighborsClassifier

# Set X_train and Y_train
X_train = [[-10, -10], [-5, -5], [0, 0], [5, 5], [10, 10], [15, 15]]
Y_train = ["Quadrado", "Quadrado", "Quadrado", "Triangulo", "Triangulo", "Triangulo"]

# Instantiating the class
knn = KNeighborsClassifier(n_neighbors=3)

# Set fit data
knn.fit(X_train, Y_train)

# Set test data
X_predict = [[2.5, 2.5], [0.5, 7.5]]

# Save predict in variable
predict = knn.predict(X_predict)

# Print predict
print(predict)