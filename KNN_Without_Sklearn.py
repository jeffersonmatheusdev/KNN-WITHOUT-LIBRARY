import math

class KNN:
    def __init__(self):
        neighbors = 1
        X_train = None
        Y_train = None

    def calcule_distance_euclidienne(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def fit(self, X_train, Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
    
    def sortOnFloat(self, sublist):
        return [v for v in sublist if isinstance(v, float)]

    def predict(self, X_test):
        n_neighbors = 5
        X_train = self.X_train
        Y_train = self.Y_train
        result = []

        for X_pos, Y_pos in X_test:
            distances = []
            for X_train_element, Y_train_element in zip(X_train, Y_train):

                distances.append(
                    [
                        self.calcule_distance_euclidienne(X_pos, Y_pos, X_train_element[0], X_train_element[1]),
                        Y_train_element
                    ]
                )
            result.append(max(sorted(distances, key=self.sortOnFloat)[:n_neighbors][::-1])[1])
        
        if len(result) == 1:
            return result[0]
        else:
            return result

if __name__ == "__main__":
    
    # Instantiating the class
    knn = KNN()

    # Set X_train and Y_train
    X_train = [[-10, -10], [-5, -5], [0, 0], [5, 5], [10, 10], [15, 15]]
    Y_train = ["Quadrado", "Quadrado", "Quadrado", "Triangulo", "Triangulo", "Triangulo"]

    # Set fit data
    fit = knn.fit(X_train, Y_train)

    # Set test data
    X_test = [[2.0, 2.5], [0.5, 7.5]]

    # Save predict in variable
    predict = knn.predict(X_test)

    # Print predict
    print(predict)