'''
Reads in ASCII art of letters A-F as training data for the neural network
Letters are two depictions of A (A1, A2), then one each of B-F
Output is six arrays of length 101 elements:
	- elements at 0-99 are the characters from the ASCII file
	- element at 100 is 1 if the characters depict an A, and 0 if not
'''


'''
1. read each file in the directory 'letters' into its own array
1a. the name of each file becomes the name of the array
1b. the characters in each file are array elements 0-99
2. add image ==A as element 100
2a. if the array name starts with A, element 100 is 
2b. else, second element is 0
'''

# list for train_set
train_set = []


with open("letters/A1") as f:
	A1 = f.read()

with open("letters/A2") as f:
	A2 = f.read()

with open("letters/B") as f:
	B = f.read()

with open("letters/C") as f:
	C = f.read()

with open("letters/D") as f:
	D = f.read()

with open("letters/E") as f:
	E = f.read()

with open("letters/F") as f:
	F = f.read()


# create combine the strings to be a single training set
def create_train_set():
	input_set = [A1, A2, B, C, D, E, F]
	output_set = [1, 1, 0, 0, 0, 0, 0]
	train_set = [input_set, output_set]
	return train_set

# return the number of inputs on each string; this is number of layer 1 neurons in network
def get_inputs_num():
	inputs_num = len(train_set)
	return inputs_num

# return the number of output neurons; for a classifier, this is the number of unique outputs
def get_outputs_num():
	return 2
'''
_____________________________________________________________________

import random

# number pairs in training dataset
num_sets = 8
# number of digits in the input
inputs_num = 4
# list for train_set
train_set = []

# create one input, output pair
def create_train_pair():
	# input list with binary digits
	inputs = [random.randint(0,1) for _ in range (inputs_num)]

	# output list of one boolean, whether count of 1s in input is even (0) or odd (1)
	input_sum = sum(inputs)
	output = [int(input_sum %2 != 0)]

	# list of the two lists
	train_pair = [inputs, output]
	return train_pair

# create the needed number of pairs for the training dataset
def create_train_set():
	for i in range (0, num_sets):
		train_set.append(create_train_pair())
	return train_set

# return the number of inputs; this is number of layer 1 neurons in network
def get_inputs_num():
	return inputs_num

# return the number of output neurons; for a classifier, this is the number of unique outputs
def get_outputs_num():
	return 2
'''


	

