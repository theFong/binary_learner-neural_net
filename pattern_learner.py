import numpy as np
import sys

def sigmoid(x):
	return 1/(1+np.exp(-x))

# approximation
def sigmoid_prime(x):
	return x*(1-x)

# inputs
X = np.array([[0,0,1],
			  [0,1,1],
			  [1,0,1],
			  [1,1,1]])

# outputs
Y = np.array([[0],
			  [1],
			  [1],
			  [0]])

np.random.seed(1)

# synapse matrices
	# random weight
syn0 = 2*np.random.random((3,4)) - 1
syn1 = 2*np.random.random((4,1)) - 1

# training
for j in xrange(60000):
	l0 = X
	l1 = sigmoid(np.dot(l0,syn0))
	l2 = sigmoid(np.dot(l1,syn1))

	l2_error = Y - l2

	if (j % 10000) == 0:
		print "Error: " + str(np.mean(np.abs(l2_error)))

    # Backpropagation
	l2_delta = l2_error*sigmoid_prime(l2)
	l1_error = l2_delta.dot(syn1.T)
	l1_delta = l1_error*sigmoid_prime(l1)

	# update weights
	syn1 += l1.T.dot(l2_delta)
	syn0 += l0.T.dot(l1_delta)

print "Output after training:"
print l2
