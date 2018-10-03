'''
Create training dataset for neural network
Training data set must be a list of two-element lists: input and output
First item is random binary digits: input to NN
Second item is one binary digit: output for NN
'''

import random

# number of input-output pairs in training dataset
# chosen by user
num_sets = 50
# number of digits in the input
# chosen by user
inputs_num = 3
# list for train_set
train_set = []

'''
# SAMPLE DATASET TYPE 1: AND Gate
def create_train_pair():
	# input list with binary digits
	inputs = [random.randint(0,1) for _ in range (inputs_num)]
	# output: AND gate of inputs
	output = int(all(inputs))
	# list of the two lists
	train_pair = [inputs, output]
	return train_pair
'''

# SAMPLE DATASET 2: Summation
def create_train_pair():
	# input list with binary digits
	inputs = [random.randint(0,1) for _ in range (inputs_num)]
	# output: sum of inputs
	output = sum(inputs)
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

# return the number of inputs; this is number of layer0 neurons in network
def get_inputs_num():
	return inputs_num

# return the number of output neurons for the network
# for a classifier, this would be the number of unique outputs
# TODO presume that nn is a classifier, CALCULATE unique outputs
def get_outputs_num():
	return 4



	

