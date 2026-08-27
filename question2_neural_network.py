import numpy as np

# --------------------------------------------------
# 1. Create Dataset
# --------------------------------------------------

# Features:
# [House Size, Bedrooms, Bathrooms, House Age,
#  Distance from City, Parking Spaces]

X = np.array([
    [1000, 2, 1, 20, 15, 1],
    [1200, 2, 2, 15, 12, 1],
    [1500, 3, 2, 10, 10, 2],
    [1800, 3, 2, 8, 8, 2],
    [2000, 4, 3, 5, 6, 2],
    [2200, 4, 3, 3, 5, 3],
    [900,  2, 1, 25, 18, 0],
    [1300, 3, 2, 12, 14, 1],
    [1600, 3, 2, 7, 9, 2],
    [1900, 4, 2, 6, 7, 2],
    [2400, 5, 3, 2, 4, 3],
    [1100, 2, 1, 18, 16, 1]
], dtype=float)

# House prices
# Price is in thousands
y = np.array([
    220,
    270,
    360,
    450,
    520,
    600,
    180,
    310,
    410,
    480,
    680,
    240
], dtype=float).reshape(-1, 1)


# --------------------------------------------------
# 2. Normalize Input Features and Target
# --------------------------------------------------

X_min = X.min(axis=0)
X_max = X.max(axis=0)

y_min = y.min()
y_max = y.max()

X_norm = (X - X_min) / (X_max - X_min)
y_norm = (y - y_min) / (y_max - y_min)


# --------------------------------------------------
# 3. Build Neural Network
# --------------------------------------------------

np.random.seed(3)

# Input layer = 6 neurons
# Hidden Layer 1 = 4 neurons
# Hidden Layer 2 = 3 neurons
# Output Layer = 1 neuron

W1 = np.random.randn(6, 4) * np.sqrt(2 / 6)
b1 = np.ones((1, 4)) * 0.1

W2 = np.random.randn(4, 3) * np.sqrt(2 / 4)
b2 = np.ones((1, 3)) * 0.1

W3 = np.random.randn(3, 1) * np.sqrt(2 / 3)
b3 = np.ones((1, 1)) * 0.1


# --------------------------------------------------
# ReLU Activation Function
# --------------------------------------------------

def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return (x > 0).astype(float)


# --------------------------------------------------
# 4. Training using Forward Propagation
#    and Backpropagation
# --------------------------------------------------

learning_rate = 0.02
epochs = 5000

for epoch in range(1, epochs + 1):

    # ---------- Forward Propagation ----------

    z1 = np.dot(X_norm, W1) + b1
    h1 = relu(z1)

    z2 = np.dot(h1, W2) + b2
    h2 = relu(z2)

    z3 = np.dot(h2, W3) + b3

    prediction = z3

    # Mean Squared Error
    loss = np.mean((prediction - y_norm) ** 2)


    # ---------- Backpropagation ----------

    # Output layer
    d3 = 2 * (prediction - y_norm) / len(X_norm)

    dW3 = np.dot(h2.T, d3)
    db3 = np.sum(d3, axis=0, keepdims=True)


    # Hidden Layer 2
    d2 = np.dot(d3, W3.T) * relu_derivative(z2)

    dW2 = np.dot(h1.T, d2)
    db2 = np.sum(d2, axis=0, keepdims=True)


    # Hidden Layer 1
    d1 = np.dot(d2, W2.T) * relu_derivative(z1)

    dW1 = np.dot(X_norm.T, d1)
    db1 = np.sum(d1, axis=0, keepdims=True)


    # ---------- Update Weights ----------

    W3 -= learning_rate * dW3
    b3 -= learning_rate * db3

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1


    # Display loss every 500 epochs
    if epoch % 500 == 0:
        print("Epoch:", epoch, "Loss:", loss)


# --------------------------------------------------
# 5. Predict New House Price
# --------------------------------------------------

new_house = np.array([
    [1800, 3, 2, 10, 8, 2]
], dtype=float)

# Normalize new house using training data parameters
new_house_norm = (new_house - X_min) / (X_max - X_min)


# Forward propagation
z1 = np.dot(new_house_norm, W1) + b1
h1 = relu(z1)

z2 = np.dot(h1, W2) + b2
h2 = relu(z2)

z3 = np.dot(h2, W3) + b3

predicted_norm = z3


# Convert normalized price back to original scale
predicted_price = (
    predicted_norm * (y_max - y_min)
) + y_min


print("\n--------------------------------")
print("HOUSE PRICE PREDICTION")
print("--------------------------------")
print("House Size: 1800")
print("Bedrooms: 3")
print("Bathrooms: 2")
print("Age: 10")
print("Distance: 8")
print("Parking: 2")

print("\nPredicted House Price:",
      round(float(predicted_price[0][0]), 2),
      "thousand")