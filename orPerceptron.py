import numpy as np

class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()
    
    def predict(self, input):
        f = np.dot(self.weights, input) + self.bias
        return 1 if f >= 0.8 else 0
    
    def train(self, inputs, target, learning_rate=0.05, epochs=100):
        for _ in range(epochs):
            for i in range(len(inputs)):
                prediction = self.predict(inputs[i])
                error = target[i] - prediction
                self.weights += (learning_rate * error * inputs[i])
                self.bias += (error*learning_rate)
        
or_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
or_targets = np.array([0, 1, 1, 1])

or_perceptron = Perceptron(2)

or_perceptron.train(or_inputs, or_targets)

test_inputs = np.array([[1, 0], [1, 1], [0,0], [0, 1]])
print("OR Perceptron\nInput\t\tOutput")
for test_input in test_inputs:
    prediction = or_perceptron.predict(test_input)
    print(f"{test_input}\t\t{prediction}")
