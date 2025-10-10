import numpy as np

# Data: simple sequence
data = np.array([1,2,3,4,5,6], dtype=float)
W_x, W_h, W_y = 0.5, 0.5, 0.5
h = 0

# Training
for epoch in range(10):
    h = 0
    for x in data[:-1]:
        h = np.tanh(W_x*x + W_h*h)
        y = W_y*h
        e = data[epoch % len(data)] - y
        W_y += 0.01*e*h

# Prediction
h = 0
for x in data:
    h = np.tanh(W_x*x + W_h*h)
pred = W_y*h
print("Next value prediction:", pred)
