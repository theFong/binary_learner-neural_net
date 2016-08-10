#Simple Pattern Learner
Alec Fong, Aug 2016

##Summary

A simple neural network to learn binary patterns

Example:
```
- Given:
[0,0,1] => 0
[1,1,1] => 1
[1,0,1] => 1
[0,1,1] => 0

- What does:
[1,0,0] => ?
```
The neural network will learn the pattern that a 1 in the 
first column of the matrix means 1 is the answer.

The neural network proof of concept trains its self 60,000 times printing its 
error every 10,000 and then prints the output layer

## Run
### Neural Network Proof of Concept
Demonstrates gradient descent by adjusting its network and displaying
its diminishing error
```
python neural_networkPOC.py
```
### Pattern Learner -> Recognizer
```
python main.py
or
python main.py [X,X,X]
```
'X' must be a binary digit ie. 1 or 0
## Neural Network

- Gradient descent
- Functions
	- sigma(z) = 1/(1+exp(-z))
	- sigma'(z) ~ x(1-x)
