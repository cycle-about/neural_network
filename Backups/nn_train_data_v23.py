'''
Create training dataset for neural network
Training data sets are a list of lists
First item is random binary digits: input to NN
Second item is one binary digit, whether inputs are all 1: output for NN
'''

import random

# number of input, output pairs in training dataset
num_sets = 50
# number of digits in the input
inputs_num = 2
# list for train_set
train_set = []

# create one input, output pair
def create_train_pair():
	# input list with binary digits
	inputs = [random.randint(0,1) for _ in range (inputs_num)]

	# output list of one boolean, value of first digit
	# output = inputs[0]

	# output: AND gate of inputs
	output = int(all(inputs))

	# list of the two lists
	train_pair = [inputs, output]
	return train_pair

# create the needed number of pairs for the training dataset
def create_train_set():
	global train_set
	train_set = []
	for i in range (0, num_sets):
		train_set.append(create_train_pair())
	return train_set

# return the number of inputs; this is number of layer 1 neurons in network
def get_inputs_num():
	return inputs_num

# return the number of output neurons for the network
# for a classifier, this would be the number of unique outputs
def get_outputs_num():
	return 1



	

