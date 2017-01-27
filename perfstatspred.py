from numpy import exp, array, random, dot
import os


class NeuralNetwork():
    def __init__(self):

        print "---> Initializing neural network"
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs.
        random.seed(os.getpid())

        # We model a single neuron, with 3 input connections and 1 output connection.
        # We assign random weights to a 3 x 1 matrix, with values in the range -1 to 1
        # and mean 0.
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

        print "---> Initialization done\n"



    # The Sigmoid function, which describes an S shaped curve.
    # We pass the weighted sum of the inputs through this function to
    # normalise them between 0 and 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    # It indicates how confident we are about the existing weight.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # We train the neural network through a process of trial and error.
    # Adjusting the synaptic weights each time.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            # Pass the training set through our neural network (a single neuron).
            output = self.think(training_set_inputs)

            # Calculate the error (The difference between the desired output
            # and the predicted output).
            error = training_set_outputs - output

            # Multiply the error by the input and again by the gradient of the Sigmoid curve.
            # This means less confident weights are adjusted more.
            # This means inputs, which are zero, do not cause changes to the weights.
            adjustment = dot(training_set_inputs.T,  error * self.__sigmoid_derivative(output))

            #print "error = " + str(error)
            #print "adjustment = " + str(adjustment)
            #print "synptic_weights = " + str(self.synaptic_weights)

            # Adjust the weights.
            self.synaptic_weights += adjustment

    # The neural network thinks.
    def think(self, inputs):
        # Pass inputs through our neural network (our single neuron).
        return self.__sigmoid(dot(inputs, self.synaptic_weights))

def normalizeList(arr):
    max_val = max(arr)
    min_val = min(arr)

    result = []

    for val in arr:
        normalized = float((val-min_val))/(max_val-min_val)
        result.append(normalized)

    return result

def denormalizeList(arr, val):
    max_val = max(arr)
    min_val = min(arr)

    denormalized = val * (max_val-min_val) + min_val

    return denormalized

def readTrace(filename):
    trace_data = [list() for x in range(3)]
    arr = []

    with open(filename, "r") as tracefile:
        for line in tracefile:
            if not "#" in line:
                currentline = line.strip().split(",")
                currentline = map(float, currentline)
                arr.append(currentline)

    #print "array = " + str(arr)
    return array(arr)


if __name__ == "__main__":

    #Intialise a single neuron neural network.
    neural_network = NeuralNetwork()

    print "---> Random starting synaptic weights after initialization = "
    print neural_network.synaptic_weights
    print "\n"

    # The training set. We have 4 examples, each consisting of 3 input values
    # and 1 output value.

    print "---> Reading input and output trace"
    training_set_inputs = readTrace("l1_dcache.trace")
    training_set_outputs = readTrace("l1_dcache.out.trace")


    print "---> Normalizing ip and op values between 0 and 1"
    length_of_input = len(training_set_inputs)
    length_of_output = len(training_set_outputs)
    normalized_training_set_inputs = [[] for i in range(length_of_input)]
    normalized_training_set_outputs = []
    #normalized_training_set_outputs = list()

    for i in range(0,3):
        lst_ip = [item[i] for item in training_set_inputs]
        returned_list = normalizeList(lst_ip)
        #print "returned = " + str(returned_list)
        for j in range(0,length_of_input):
            normalized_training_set_inputs[j].append(returned_list[j])


    returned_list = normalizeList(training_set_outputs)
    #for item in returned_lit:
    #    normalized_training_set_outputs.append(item[0])

    for i in range(0,length_of_output):
        normalized_training_set_outputs.append(returned_list[i])

    normalized_training_set_inputs = array(normalized_training_set_inputs)
    normalized_training_set_outputs = array(normalized_training_set_outputs)

    #print "Normalized training set ip = " + str(normalized_training_set_inputs)


    #print "Normalized training set op = " + str(normalized_training_set_outputs)

    #print "IP dimension = " + str(normalized_training_set_inputs.shape)
    #print "OP dimension = " + str(normalized_training_set_outputs.shape)

    print "---> Normalization done"



    # Train the neural network using a training set.
    # Do it 10,000 times and make small adjustments each time.
    print "---> Training neural network with normalized ip and op"
    neural_network.train(normalized_training_set_inputs, normalized_training_set_outputs, 10000)



    print "---> New synaptic weights after training: "
    print neural_network.synaptic_weights



    print "---> Training done\n"



    # Test the neural network with a new situation.
    print "---> Testing with new input"

    new_input = array([0, 22729, 23345])
    new_input_normalized = normalizeList(new_input)

    print "Considering new input = " + str(new_input)

    normalized_result = neural_network.think(new_input)

    print "\n**** RESULT *****"
    print "Normalized = " + str(normalized_result)
    print "Denormalized = " + str(denormalizeList(training_set_outputs, normalized_result[0]))
    print "**** END RESULT *****"




