# Neural Network step 1
# 1. create object for preceptron/neuron
# 2. create contstructor that takes N inputs for preceptron
# 3. initialize weights to something
# 4. function run that creates the neuron's output
# 5. function update to modify weights and biases


import math

# number of neurons in each layer of network
layer = 10

# NEURON CLASS
class Neuron():
	# constructor - each neuron has a list of weights from connetions to prior layer, and a bias
	def __init__(self, w=[0.5]*layer, b=1.0):
		self.weights = w
		self.bias = b

# sigmoid function for output of neuron
def sigmoid(x):
	return 1/(1+math.e**-x)

# activation function to generate the output of the neuron
# input is neuron, list of outputs from all neurons in prior layer, list of weights of the connections
def run(n, inputs):
	sum = 0
	for i in range(0, len(inputs)):
		sum += inputs[i] * n.weights[i]
	sum += n.bias
	n.output = sigmoid(sum)
	return n.output
	
# update neuron with new weights and bias
# input is neuron, list of floats for new weights, float for new bias
def update(n, w, b):
	n.weights = w
	n.bias = b


# DEMO
# list of simulated inputs for neuron
inputs = [0.8] * layer

neuron0 = Neuron()

print 'Neuron\'s default bias: ', neuron0.bias
print 'Neuron\'s default weights from prior layer: ', neuron0.weights
print 'Neuron\'s default output', run(neuron0, inputs)

update(neuron0, [0.4]*layer, 0.9)

print ''
print 'Neuron\'s updated bias: ', neuron0.bias
print 'Neuron\'s updated weights from prior layer: ', neuron0.weights
print 'Neuron\'s updated output', run(neuron0, inputs)


