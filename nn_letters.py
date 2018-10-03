'''
Neural network
Neuron objects are arranged in a list of lists
Neurons to take input, calculate output, and pass output to the next layer's neurons
Training data is from nn_train_data.py
'''

# nn_train_data generates and sends info on the training data
import math, nn_letters_train, nn_lib

# depth of each layer. First is input layer, last is output layer
# input and output layer sizes are determined by training dataset from nn_train_data.py
input_num = nn_letters_train.get_inputs_num() 
output_num = nn_letters_train.get_outputs_num() 
layer_depths = [input_num, 3, 3, output_num]
# depth of the network is the greatest layer depth
net_depth = max(layer_depths)
# number of layers in network is the length of the depths list
net_layer = len(layer_depths)
# each weight initialized to same value
initial_weight = 0.5
# each neuron's bias initialized to same value
initial_bias = 0.1
# learning rate
N = 0.5

# create and display training dataset from nn_train_data.py
train_data = nn_letters_train.create_train_set()
print 'Training Data: ASCII art of a letter'
print 'Output 1 if the image is an A, and 0 if it is not','\n\n'
for elem in train_data:
	print elem
print ''

# initialize a network
net0 = nn_lib.Net(net_depth, net_layer, layer_depths, initial_weight, initial_bias, N)

# one time only before running, set weights and biases to unique values of neuron's location
net0.set_wb()

# train the network
net0.train(train_data)


