import torch
import torch.nn.functional as F
from torch import Tensor, nn

torch.manual_seed(42)

class MNIST_CNN(nn.Module):
    def __init__(self):
        super().__init__()      
        self.conv1 = nn.Sequential(         
            nn.Conv2d(
                in_channels=1,              
                out_channels=16,            
                kernel_size=5,              
                stride=1,                   
                padding=2,                  
            ),                              
            nn.ReLU(),    
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(
            in_channels=16,
            out_channels=32,
            kernel_size=5,
            stride=1,
            padding=2
            ),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.conv3 = nn.Sequential(
            nn.Conv2d(
            in_channels=32,
            out_channels=64,
            kernel_size=5,
            stride=1,
            padding=2
            ),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )           
        self.fc1 = nn.Sequential(
            nn.Linear(64 * 7 * 7, 250),
            nn.ReLU(),
            nn.Dropout(0.2))
        self.fc2 = nn.Sequential(
            nn.Linear(250, 100),
            nn.ReLU(),
            nn.Dropout(0.2))
        self.fc3 = nn.Linear(100, 10)    
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = x.view(-1, 64 * 7 * 7) 
        x = self.fc1(x)
        x = self.fc2(x)      
        return F.log_softmax(self.fc3(x), dim=1)