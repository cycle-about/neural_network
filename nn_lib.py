import math

error_list = []
all_net_errors = []

class Neuron():
	# attributes - weights array (from prior layer connections), bias, output
	# methods - activation function, update neuron's weight and bias 
	def __init__(self, net_depth, initial_weight, initial_bias):
		self.weights = initial_weight * net_depth
		self.bias = initial_bias
		self.delta = None

	# layer0 activation function - pass through layer only
	# outputs are the inputs from the training dataset
	def activate_layer0(self, layer0_input):
		self.output = layer0_input
		print 'Output', self.output,'\n'


	# layer1-layerN activation function - neurons in all other layers get list of prior layer's outputs
	def activate(self, inputs):
		# 1. get sum of products of each input*weight
		products = 0
		for i in range(0, len(inputs)):
			# print 'input is', inputs[i], 'weight is', self.weights[i]
			products += inputs[i] * self.weights[i]
		# 2. add neuron's bias
		products += self.bias
		# 3. sigmoid on sum becomes output
		self.output = 1/(1+math.exp(-products))
		print 'Output', self.output,'\n'

	# get error of an output neuron
	def output_error(self, expected):
		x = self.output
		err = expected - self.output
		return err

	# get delta of a neuron
	def get_delta(self, err):
		x = err
		der_output  = 2 * math.exp(-x) / ((1 + math.exp(-x)) ** 2)
		self.delta = der_output * err
		print 'Delta', self.delta,'\n'

	# get error of a middle neuron
	def middle_error(self, weights, deltas):
		err = 0
		print 'Input weights', weights
		print 'Input deltas', deltas
		for i in range(len(deltas)):
			err += weights[i] * deltas[i]
		return err

	# update neuron with new weights and bias
	def update(self, w, b):
		self.weights = w
		self.bias = b

# Net is composed of Neuron objects arranged in a list of lists
# dimensions of network are net_depth * net_layer
# neurons to be ignored in each layer are skipped by run function
class Net():
	# attributes - global layers, global depth, network of neurons (a 2D array for indexing)
	# methods - run
	def __init__(self, net_depth, net_layer, layer_depths, initial_weight, initial_bias, N):
		self.network = [[Neuron(net_depth, initial_weight, initial_bias) for j in range(net_depth)] for i in range(net_layer)]
		self.net_depth = net_depth
		self.net_layer = net_layer
		self.layer_depths = layer_depths
		self.N = N

	# update each neuron to have bias of its depth
	# and input weight array with each element the depth of the sending neuron
	def set_wb(self):
		n_weights = range(0, self.net_depth)
		for i in range(0, self.net_layer):
			for j in range(0, self.net_depth):
				n_bias = j
				self.network[i][j].update(n_weights, n_bias)

	# inputs to layer0 passed in, from training dataset
	# run function skips neurons that are greater than that layer's depth 
	def feedforward(self, layer0_inputs):
		print '\nFORWARD PASS'
		for i in range(0, self.net_layer):
			# goes only to depth of that layer
			for j in range(0, self.layer_depths[i]):
				# layer0 neurons call their unique activation function
				if i==0:
					print 'Neuron index', i, j,':',
					print 'Pass through, no input weights'
					self.network[i][j].activate_layer0(layer0_inputs[j])
				else:
					print 'Neuron index', i, j,':',
					print 'Start weights', self.network[i][j].weights
					inputs = []
					for k in range(0, self.layer_depths[i-1]):
						inputs.append(self.network[i-1][k].output)
					self.network[i][j].activate(inputs)

	def backprop(self, expected):
		print '\n\nBACKWARD PASS'
		# backprop runs back to front in the network
		# does not run on layer0
		for i in range(self.net_layer-1, 0, -1):
			for j in range(0, self.layer_depths[i]):
				# output neurons call their own activation function
				if i == self.net_layer-1:
					print 'Output neuron index', i, j,':',
					error = self.network[i][j].output_error(expected)
					self.network[i][j].get_delta(error)
				else:
					print 'Middle neuron index', i, j,':',
					err = 0.0
					prior_weights = []
					prior_deltas = []
					for k in range(0, self.layer_depths[i+1]):
						prior_weights.append(self.network[i][k].weights[j])
						prior_deltas.append(self.network[i+1][k].delta)
					error = self.network[i][j].middle_error(prior_weights, prior_deltas)
					self.network[i][j].get_delta(error)

	def get_updates(self):
		# do not update layer0
		for i in range(1, self.net_layer):
			for j in range(0, self.layer_depths[i]):	
				new_weights = []
				for k in range(0, self.layer_depths[i-1]):
					new_weights.append(self.N * self.network[i][j].delta * self.network[i-1][k].output)
				new_bias = self.N * self.network[i][j].delta
				self.network[i][j].update(new_weights, new_bias)
				print 'Index', i, j, ':', self.network[i][j].weights

	def get_sq_error(self, expected):
		sq_err = 0.0
		for i in range(0, self.net_layer):
			for j in range(0, self.layer_depths[i]):
				sq_err += 0.5*(expected - self.network[i][j].output)**2
		error_list.append(sq_err)					

	def get_mean_error(self):
		mean_error = 0.0
		for i in error_list:
			mean_error += i
		mean_error /= len(error_list)
		print '\n\nPERFORMANCE\nMean error:', mean_error,'\n\n'
		return mean_error

	def train(self, train_data):
		# run network for all inputs sets in the training data
		for i in range(0, len(train_data)):
			print '________________________________\n\nRun', i
			layer0_inputs = train_data[i][0]		
			# expected = int(''.join(map(str,train_data[i][1])))
			expected = train_data[i][1]
			print 'Input:', layer0_inputs
			print 'Correct output:', expected,'\n'
			self.feedforward(layer0_inputs)
			self.backprop(expected)
			print '\nUPDATED WEIGHTS'
			self.get_updates()
			self.get_sq_error(expected)
			run_error = self.get_mean_error()  
			all_net_errors.append(run_error)


# print results of the training
print 'TRAINING THE NETWORK'
for i in range(0, len(all_net_errors)):
	print 'Run', i, 'error:', all_net_errors[i]

