import numpy as np

# Input (XOR)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# Random weights
w1, w2 = np.random.rand(2,2), np.random.rand(2,1)

# Activation
def sigmoid(x): return 1/(1+np.exp(-x))
def dsigmoid(x): return x*(1-x)

# Train
for _ in range(5000):
    # Forward
    h = sigmoid(X.dot(w1))
    o = sigmoid(h.dot(w2))
    # Backward
    e = y - o
    w2 += h.T.dot(e * dsigmoid(o)) * 0.1
    w1 += X.T.dot((e.dot(w2.T) * dsigmoid(h))) * 0.1

print("Output:\n", o.round(3))
