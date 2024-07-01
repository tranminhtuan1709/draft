import torch
import PIL

class EdgeDetection(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=1, kernel_size=3, stride=1, padding=0)
        conv1_weight = torch.tensor([[[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]],
                                     [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]],
                                     [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]],
                                     dtype=torch.float)
        conv1_bias = torch.tensor([0], dtype=torch.float)
        self.conv1.weight = torch.nn.Parameter(conv1_weight)
        self.conv1.bias = torch.nn.Parameter(conv1_bias)
        
    def forward(self, input_matrix):
        input_matrix = self.conv1(input_matrix)
        return input_matrix

# [[[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]],
# [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]],
# [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]]