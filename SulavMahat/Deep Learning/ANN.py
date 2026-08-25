import numpy as np

# -----------------------------
# House Dataset
# Features:
# Size, Bedrooms, Bathrooms,
# Age, Distance, Parking
# Target: Price (in $1000)
# -----------------------------

X = np.array([
    [1400, 2, 1, 20, 15, 1],
    [1600, 3, 2, 15, 12, 1],
    [1800, 3, 2, 10, 8, 2],
    [2000, 4, 3, 8, 6, 2],
    [2200, 4, 3, 5, 5, 2],
    [2500, 4, 4, 4, 4, 3],
    [2800, 5, 4, 3, 3, 3],
    [3000, 5, 5, 2, 2, 4]
], dtype=float)

y = np.array([
    [250],
    [300],
    [380],
    [450],
    [500],
    [620],
    [720],
    [800]
], dtype=float)

# -----------------------------
# Normalize Features
# -----------------------------

X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)

X = (X - X_mean) / X_std

# Normalize target
y_mean = np.mean(y)
y_std = np.std(y)

y = (y - y_mean) / y_std

# -----------------------------
# Activation Functions
# -----------------------------

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return (x > 0).astype(float)

# -----------------------------
# Network Architecture

# -----------------------------

input_size = 6
hidden1_size = 4
hidden2_size = 3
output_size = 1

np.random.seed(42)

W1 = np.random.randn(input_size, hidden1_size) * 0.1
b1 = np.zeros((1, hidden1_size))

W2 = np.random.randn(hidden1_size, hidden2_size) * 0.1
b2 = np.zeros((1, hidden2_size))

W3 = np.random.randn(hidden2_size, output_size) * 0.1
b3 = np.zeros((1, output_size))

learning_rate = 0.01
epochs = 500

# -----------------------------
# Training
# -----------------------------

for epoch in range(epochs):

    # Forward Propagation

    Z1 = np.dot(X, W1) + b1
    A1 = relu(Z1)

    Z2 = np.dot(A1, W2) + b2
    A2 = relu(Z2)

    Z3 = np.dot(A2, W3) + b3
    predictions = Z3

    # Loss

    loss = np.mean((predictions - y) ** 2)

    # -------------------------
    # Backpropagation
    # -------------------------

    m = len(X)

    dZ3 = (2 / m) * (predictions - y)

    dW3 = np.dot(A2.T, dZ3)
    db3 = np.sum(dZ3, axis=0, keepdims=True)

    dA2 = np.dot(dZ3, W3.T)
    dZ2 = dA2 * relu_derivative(Z2)

    dW2 = np.dot(A1.T, dZ2)
    db2 = np.sum(dZ2, axis=0, keepdims=True)

    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * relu_derivative(Z1)

    dW1 = np.dot(X.T, dZ1)
    db1 = np.sum(dZ1, axis=0, keepdims=True)

    # -------------------------
    # Update Parameters
    # -------------------------

    W3 -= learning_rate * dW3
    b3 -= learning_rate * db3

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    if epoch % 500 == 0:
        print(f"Epoch {epoch}  Loss: {loss:.6f}")

# -----------------------------
# Predict a New House
# -----------------------------

new_house = np.array([[1800, 3, 2, 10, 8, 2]])

new_house = (new_house - X_mean) / X_std

A1 = relu(np.dot(new_house, W1) + b1)
A2 = relu(np.dot(A1, W2) + b2)
prediction = np.dot(A2, W3) + b3

# Convert back to original scale
prediction = prediction * y_std + y_mean

print("\nPredicted House Price:")
print(f"${prediction[0][0] * 1000:.2f}")