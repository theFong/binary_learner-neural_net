import numpy as np

class NeuralNetwork_v0(object):
	def __init__(self):
		np.random.seed(1)

		# synapses matrices
			# random weight
		self.synapses = 2*np.random.random((3,1)) - 1

	def sigmoid(self,x):
		return 1/(1+np.exp(-x))

	# approximation of the deriv of sigmoid
	def sigmoid_prime(self,x):
		return x*(1-x)

	def train(self,training_inputs,training_outputs,training_iterations):
		for i in xrange(training_iterations):
			output_layer = self.think(training_inputs)

			# Backpropagation
			output_layer_error = training_outputs - output_layer
			output_layer_delta = output_layer_error*self.sigmoid_prime(output_layer)
			adjustment = training_inputs.T.dot(output_layer_delta)

			#Adjustment
			self.synapses += adjustment


	def think(self, inputs):
		return self.sigmoid(np.dot(inputs,self.synapses))