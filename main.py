from NeuralNetwork_v0 import NeuralNetwork_v0
import numpy as np
import sys

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

if len(sys.argv) > 1:
	testList = []
	get = sys.argv[1]
	for x in get:
		if x != "," and x != "[" and x != "]":
			testList.append(int(x))
	if len(testList) > 3:
		raise ValueError("There appears to be something wrong with your entry.")
	print "When given "+str(testList)+", the neural networks computes the answer to be: "
	print "*** 1 ***" if neural_net.think(np.array([testList[0],testList[1],testList[2]])) > .75 else "*** 0 ***"
	print "Given the output layer: "+str(neural_net.think(np.array([testList[0],testList[1],testList[2]])))
else:
	print "When given [1,0,0], the neural networks computes the answer to be: "
	print "*** 1 ***" if neural_net.think(np.array([1,0,0])) > .75 else "*** 0 ***"
	print "Given the output layer: "+str(neural_net.think(np.array([1,0,0])))