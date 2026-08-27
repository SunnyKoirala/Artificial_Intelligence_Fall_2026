import numpy as np

X = np.array([
    [1200, 2, 1, 15, 12, 1],
    [1500, 3, 2, 10, 10, 1],
    [2000, 4, 3, 5, 5, 2],
    [2500, 4, 3, 2, 3, 2],
    [1100, 2, 1, 20, 15, 0],
    [1700, 3, 2, 8, 7, 2],
    [2200, 3, 2, 4, 6, 1],
    [3000, 5, 4, 1, 2, 3]
], dtype=float)

y = np.array([[200000], [270000], [380000], [480000], [180000], [310000], [390000], [580000]], dtype=float)

X_min, X_max = X.min(axis=0), X.max(axis=0)
y_min, y_max = y.min(), y.max()

X_norm = (X - X_min) / (X_max - X_min)
y_norm = (y - y_min) / (y_max - y_min)

np.random.seed(42)
W1 = np.random.randn(6, 4) * 0.1
b1 = np.zeros((1, 4))
W2 = np.random.randn(4, 3) * 0.1
b2 = np.zeros((1, 3))
W3 = np.random.randn(3, 1) * 0.1
b3 = np.zeros((1, 1))

lr = 0.05
epochs = 2500

def relu(x):
    return np.maximum(0, x)

def relu_deriv(x):
    return (x > 0).astype(float)

for epoch in range(1, epochs + 1):
    z1 = np.dot(X_norm, W1) + b1
    a1 = relu(z1)
    
    z2 = np.dot(a1, W2) + b2
    a2 = relu(z2)
    
    z3 = np.dot(a2, W3) + b3
    a3 = z3
    
    loss = np.mean((a3 - y_norm) ** 2)
    
    if epoch % 500 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.6f}")
        
    dz3 = 2 * (a3 - y_norm) / X_norm.shape[0]
    dW3 = np.dot(a2.T, dz3)
    db3 = np.sum(dz3, axis=0, keepdims=True)
    
    da2 = np.dot(dz3, W3.T)
    dz2 = da2 * relu_deriv(z2)
    dW2 = np.dot(a1.T, dz2)
    db2 = np.sum(dz2, axis=0, keepdims=True)
    
    da1 = np.dot(dz2, W2.T)
    dz1 = da1 * relu_deriv(z1)
    dW1 = np.dot(X_norm.T, dz1)
    db1 = np.sum(dz1, axis=0, keepdims=True)
    
    W3 -= lr * dW3
    b3 -= lr * db3
    W2 -= lr * dW2
    b2 -= lr * db2
    W1 -= lr * dW1
    b1 -= lr * db1

sample_house = np.array([[1800, 3, 2, 10, 8, 2]], dtype=float)
sample_norm = (sample_house - X_min) / (X_max - X_min)

z1 = np.dot(sample_norm, W1) + b1
a1 = relu(z1)
z2 = np.dot(a1, W2) + b2
a2 = relu(z2)
pred_norm = np.dot(a2, W3) + b3

pred_price = pred_norm[0, 0] * (y_max - y_min) + y_min
print(f"Predicted House Price: ${pred_price:.2f}")
