import NeuralNetwork as nn
import numpy as np
import matplotlib.pyplot as plot

with np.load('/home/kimba/Desktop/Repo/OriamPortfolio/NumberPrediction/mnist.npz') as data:
    training_images = data['training_images']
    training_labels = data['training_labels']

    # print(training_images.shape)
    # print(training_labels.shape)
    


layer_sizes = (784,5,10)

'''simulated input'''
# x = np.ones((layer_sizes[0],1))

net = nn.NeuralNetwork(layer_sizes)
prediction = net.predict(training_images)

'''prints the dimension of the matrix'''
# print(prediction.shape)

#prints the highest prediciton - in this case also the number that it believes that it is
print('Number is a {} with ({:.2f}%) confidence'.format( np.argmax(prediction[0]) , prediction[0][np.argmax(prediction[0])][0]*100))

net.print_accuracy(training_images,training_labels)

'''Training Function'''
# net.trainingFunction(training_images,training_labels)



'''visualization code:'''
i = 0
plot.imshow(training_images[i].reshape(28,28), cmap = 'gray')
plot.title(f"Guess: {np.argmax(prediction[i])}  Actual: {np.argmax(training_labels[0])}")
# plot.show()


''' training attempt '''

net.save_weights()

