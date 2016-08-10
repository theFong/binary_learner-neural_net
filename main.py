from NeuralNetwork_v0 import NeuralNetwork_v0
import numpy as np

neural_net = NeuralNetwork_v0()

print "Random starting synapse weights: "
print neural_net.synapses

training_set_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = np.array([[0],
		 						 [1],
								 [1],
		  						 [0]])

neural_net.train(training_set_inputs, training_set_outputs, 10000)

print "Adjusted weights after training: "
print neural_net.synapses

print "When given [1,0,0], the neural networks computes: "
print neural_net.think(np.array([1,0,0]))