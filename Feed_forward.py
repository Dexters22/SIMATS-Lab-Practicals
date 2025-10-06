import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (XOR problem)
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Initialize weights and biases randomly
np.random.seed(42)
input_layer_size = 2
hidden_layer_size = 2
output_layer_size = 1

W1 = np.random.uniform(size=(input_layer_size, hidden_layer_size))
b1 = np.random.uniform(size=(1, hidden_layer_size))
W2 = np.random.uniform(size=(hidden_layer_size, output_layer_size))
b2 = np.random.uniform(size=(1, output_layer_size))

# Training
epochs = 10000
learning_rate = 0.1

for _ in range(epochs):
    # Forward Pass
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    final_output = sigmoid(final_input)

    # Error calculation
    error = y - final_output

    # Backpropagation
    d_output = error * sigmoid_derivative(final_output)
    d_hidden = d_output.dot(W2.T) * sigmoid_derivative(hidden_output)

    # Update weights and biases
    W2 += hidden_output.T.dot(d_output) * learning_rate
    b2 += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    W1 += X.T.dot(d_hidden) * learning_rate
    b1 += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

# Final predictions
print("\nPredicted Output after training:")
print(final_output)
