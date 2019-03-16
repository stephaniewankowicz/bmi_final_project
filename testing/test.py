import sys
import numpy as np
sys.path.append('../scripts/')
from scripts import NN

#testing the autoencoder
x = np.identity(8)
y = np.identity(8)
NN_auto = NN.Neural_Network(input_layer_size=8, hidden_layer_size=3, output_layer_size=8, Lambda=2e-6)
NN_auto.train(x,y,10000,0.45)
predict=NN.forward(x)
assert np.array_equal(x, print(predict.round())
