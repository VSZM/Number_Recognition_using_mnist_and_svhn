import mnist_loader
import network
import pickle
import os.path
import util

MODEL_FILE_NAME = 'network_model.pkl'
EPOCHS = 2
HIDDEN_LAYER_SIZE = 100
LEARNING_RATE = 3.0


def teach_network(training_data, test_data):
    print 'Teaching network. Epochs = |{}|, Hidden layer size = |{}|, Learning rate = |{}|'.format(EPOCHS, HIDDEN_LAYER_SIZE, LEARNING_RATE)
    nn = load_network()
    nn.SGD(training_data, EPOCHS, 10, LEARNING_RATE, test_data=test_data)
    return nn

def load_network():
    nn = network.Network([784, HIDDEN_LAYER_SIZE, 10])
    if os.path.exists(MODEL_FILE_NAME):
        print 'Loading previous model..'
        nn.load_model(MODEL_FILE_NAME)
    return nn

if __name__ == '__main__':
    print 'Getting data...'
    training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
    nn =  load_network()
    util.evaluate_image(nn, '6big.png')
    