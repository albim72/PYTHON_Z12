import numpy as np

class SimpleNeuralNetwork:
    def __init__(self):
        np.random.seed(1)
        self.weights = 2*np.random.random((3,1))-1
        
    #funkcja sigmoid
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))
    
    #różniczka sigmoid
    def d_sigmoid(self,x):
        return x*(1-x)
    
    def train(self,train_input,train_output,train_iters):
        for _ in range(train_iters):
            propagation_result = self.propagation(train_input)
            self.backward_propagation(propagation_result,train_input,train_output)
            
    def propagation(self,inputs):
        return self.sigmoid(np.dot(inputs.astype(float),self.weights))
    
    def backward_propagation(self,propagation_result,train_input,train_output):
        error = train_output - propagation_result
        self.weights += np.dot(train_output.T,error*self.d_sigmoid(propagation_result))