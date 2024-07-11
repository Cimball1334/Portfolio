import NeuralNetwork as nn
import numpy as np
import matplotlib.pyplot as plot

layer_sizes = (784,5,10)
net = nn.NeuralNetwork(layer_sizes)

with np.load('/home/kimba/Desktop/Repo/OriamPortfolio/NumberPrediction/mnist.npz') as data:
    training_images = data['training_images']
    training_labels = data['training_labels']

# prediction = net.predict(training_images)

# print(prediction.shape)

layer_sizes = (784,5,10)

net = nn.NeuralNetwork(layer_sizes)
prediction = net.predict(training_images)