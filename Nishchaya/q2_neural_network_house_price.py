import numpy as np

np.random.seed(42)

def relu(z):
    return np.maximum(0, z)

def relu_derivative(z):
    return (z > 0).astype(float)

def main():
    print("=" * 65)
    print("QUESTION 2: NEURAL NETWORK FOR HOUSE PRICE PREDICTION")
    print("=" * 65)

    
    X_raw = np.array([
        [1200, 2, 1.0, 15, 12, 1],
        [1500, 3, 2.0,  8, 10, 2],
        [2000, 4, 2.5,  5,  5, 2],
        [2500, 4, 3.0,  2,  3, 3],
        [1100, 2, 1.0, 20, 15, 1],
        [1750, 3, 2.0, 12,  9, 2],
        [2200, 3, 2.5,  4,  6, 2],
        [3000, 5, 3.5,  1,  2, 3]
    ], dtype=float)

    y_raw = np.array([
        [220000],
        [310000],
        [420000],
        [550000],
        [190000],
        [340000],
        [460000],
        [680000]
    ], dtype=float)

    print("\n1. Sample Dataset:")
    print("   Input Features Shape:", X_raw.shape)
    print("   Target Prices Shape: ", y_raw.shape)
    
    X_min = X_raw.min(axis=0)
    X_max = X_raw.max(axis=0)
    X_norm = (X_raw - X_min) / (X_max - X_min)

    y_min = y_raw.min()
    y_max = y_raw.max()
    y_norm = (y_raw - y_min) / (y_max - y_min)

    print("\n2. Normalized Features and Target Values successfully.")

    W1 = np.random.randn(6, 4) * np.sqrt(2.0 / 6)
    b1 = np.zeros((1, 4))

    W2 = np.random.randn(4, 3) * np.sqrt(2.0 / 4)
    b2 = np.zeros((1, 3))

    W3 = np.random.randn(3, 1) * np.sqrt(2.0 / 3)
    b3 = np.zeros((1, 1))

    epochs = 3000
    learning_rate = 0.05
    N = X_norm.shape[0]

    print("\n3. Network Architecture:")
    print("   Input Layer:  6 neurons")
    print("   Hidden L1:    4 neurons (ReLU)")
    print("   Hidden L2:    3 neurons (ReLU)")
    print("   Output Layer: 1 neuron (Linear)")

    print("\n4 & 5. Training Network (Displaying loss every 500 epochs):")
    print("-" * 45)

    for epoch in range(1, epochs + 1):
        Z1 = np.dot(X_norm, W1) + b1
        A1 = relu(Z1)

        Z2 = np.dot(A1, W2) + b2
        A2 = relu(Z2)

        Z3 = np.dot(A2, W3) + b3
        A3 = Z3 

        loss = np.mean((A3 - y_norm) ** 2)

        dZ3 = (2 / N) * (A3 - y_norm)

        dW3 = np.dot(A2.T, dZ3)
        db3 = np.sum(dZ3, axis=0, keepdims=True)

        dA2 = np.dot(dZ3, W3.T)
        dZ2 = dA2 * relu_derivative(Z2)

        dW2 = np.dot(A1.T, dZ2)
        db2 = np.sum(dZ2, axis=0, keepdims=True)

        dA1 = np.dot(dZ2, W2.T)
        dZ1 = dA1 * relu_derivative(Z1)

        dW1 = np.dot(X_norm.T, dZ1)
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        W3 -= learning_rate * dW3
        b3 -= learning_rate * db3
        W2 -= learning_rate * dW2
        b2 -= learning_rate * db2
        W1 -= learning_rate * dW1
        b1 -= learning_rate * db1

        if epoch % 500 == 0 or epoch == 1:
            print(f"   Epoch {epoch:4d}/{epochs} | Training Loss (MSE): {loss:.6f}")

    print("-" * 45)

    test_house_raw = np.array([[1800, 3, 2, 10, 8, 2]], dtype=float)
    
    test_house_norm = (test_house_raw - X_min) / (X_max - X_min)

    z1_test = np.dot(test_house_norm, W1) + b1
    a1_test = relu(z1_test)

    z2_test = np.dot(a1_test, W2) + b2
    a2_test = relu(z2_test)

    z3_test = np.dot(a2_test, W3) + b3
    predicted_norm_price = z3_test[0, 0]

    predicted_price = predicted_norm_price * (y_max - y_min) + y_min

    print("\n6 & 7. Prediction for Test House:")
    print("   House Details:")
    print("     - Size:             1800 sq ft")
    print("     - Bedrooms:         3")
    print("     - Bathrooms:        2")
    print("     - Age:              10 years")
    print("     - Distance to City: 8 miles")
    print("     - Parking Spaces:   2")
    print("-" * 45)
    print(f"   Predicted Normalized Output: {predicted_norm_price:.4f}")
    print(f"   Predicted House Price:      ${predicted_price:,.2f}")
    print("=" * 65)

if __name__ == "__main__":
    main()
