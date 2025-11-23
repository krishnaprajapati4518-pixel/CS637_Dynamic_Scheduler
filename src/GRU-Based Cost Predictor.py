import torch
from torch import nn

class CostPredictor(nn.Module):
    def __init__(self, in_dim, hid_dim, out_dim):
        super().__init__()
        self.gru = nn.GRU(in_dim, hid_dim, batch_first=True)
        self.fc = nn.Linear(hid_dim, out_dim)

    def forward(self, x):
        out, _ = self.gru(x)
        return self.fc(out[:, -1, :])
