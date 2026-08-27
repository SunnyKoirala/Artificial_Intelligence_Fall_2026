import numpy as np

# ---------------------------
# Dataset
# ---------------------------

X = np.array([
    [1000, 2, 1, 20, 15, 1],
    [1200, 2, 1, 15, 12, 1],
    [1500, 3, 2, 10, 10, 1],
    [1800, 3, 2, 8, 8, 2],
    [2000, 4, 3, 5, 5, 2],
    [2200, 4, 3, 4, 4, 2],
    [2500, 5, 3, 2, 3, 3],
    [2800, 5, 4, 1, 2, 3]
], dtype=float)

# House prices
y = np.array([
    [150000],
    [180000],
    [230000],
    [280000],
    [320000],
    [350000],
    [400000],
    [450000]
], dtype=float)

# ---------------------------
# Normalize Data
# ---------------------------

X_min = X.min(axis=0)
X_max = X.max(axis=0)

X_norm = (X - X_min) / (X_max - X_min)

y_min = y.min()
y_max = y.max()

y_norm = (y - y_min) / (y_max - y_min)

# ---------------------------
# Initialize Weights
# ---------------------------

np.random.seed(42)

# Input layer = 6
# Hidden layer 1 = 4
W1 = np.random.randn(6, 4) * 0.1
b1 = np.zeros((1, 4))

# Hidden layer 2 = 3
W2 = np.random.randn(4, 3) * 0.1
b2 = np.zeros((1, 3))

# Output layer = 1
W3 = np.random.randn(3, 1) * 0.1
b3 = np.zeros((1, 1))


# ---------------------------
# ReLU Activation
# ---------------------------

def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return (x > 0).astype(float)


# ---------------------------
# Training
# ---------------------------

learning_rate = 0.05
epochs = 5000

for epoch in range(epochs):

    # Forward Propagation

    z1 = np.dot(X_norm, W1) + b1
    a1 = relu(z1)

    z2 = np.dot(a1, W2) + b2
    a2 = relu(z2)

    output = np.dot(a2, W3) + b3

    # Calculate loss
    loss = np.mean((y_norm - output) ** 2)

    # ---------------------------
    # Backpropagation
    # ---------------------------

    output_error = output - y_norm

    dW3 = np.dot(a2.T, output_error)
    db3 = np.sum(output_error, axis=0, keepdims=True)

    hidden2_error = np.dot(output_error, W3.T)
    hidden2_delta = hidden2_error * relu_derivative(z2)

    dW2 = np.dot(a1.T, hidden2_delta)
    db2 = np.sum(hidden2_delta, axis=0, keepdims=True)

    hidden1_error = np.dot(hidden2_delta, W2.T)
    hidden1_delta = hidden1_error * relu_derivative(z1)

    dW1 = np.dot(X_norm.T, hidden1_delta)
    db1 = np.sum(hidden1_delta, axis=0, keepdims=True)

    # ---------------------------
    # Update Weights
    # ---------------------------

    W3 -= learning_rate * dW3
    b3 -= learning_rate * db3

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    # Display loss every 500 epochs
    if epoch % 500 == 0:
        print("Epoch:", epoch, "Loss:", loss)


# ---------------------------
# Prediction
# ---------------------------

new_house = np.array([
    [1800, 3, 2, 10, 8, 2]
], dtype=float)

# Normalize new house
new_house_norm = (new_house - X_min) / (X_max - X_min)

# Forward propagation
z1 = np.dot(new_house_norm, W1) + b1
a1 = relu(z1)

z2 = np.dot(a1, W2) + b2
a2 = relu(z2)

predicted_normalized = np.dot(a2, W3) + b3

# Convert normalized price back to real price
predicted_price = predicted_normalized * (y_max - y_min) + y_min

print("\nPredicted House Price:")
print(predicted_price[0][0])