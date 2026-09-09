import torch
import torch.nn as nn

# create first layer of neuro netwrok
class MyFirstLayer():
    def __init__(self,input_dim, output_dim):
        self.W = nn.Parameter(torch.randn(input_dim, output_dim, requires_grad = True))
        self.b = nn.Parameter(torch.randn(1,output_dim,requires_grad= True))

    def forward(self,inputs):
        z = inputs @ self.W + self.b

        self.output = torch.sigmoid(z)
        return self.output
    def grad_descent(self,target, learning_rate):
        i = 0
        while i < 1000:
            loss = nn.functional.cross_entropy(self.output,target)
            loss.backward() 
            