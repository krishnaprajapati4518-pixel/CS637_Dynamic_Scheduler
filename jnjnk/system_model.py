from scipy.linalg import expm
import numpy as np

class SystemModel:
    def __init__(self, Phi, Gamma, h):
        self.Phi = np.array(Phi)
        self.Gamma = np.array(Gamma)
        self.h = h
        self.A = None
        self.B = None

    def discretize(self):
        self.A = expm(self.Phi * self.h)
        self.B = np.dot(np.linalg.inv(self.Phi), (self.A - np.eye(self.Phi.shape[0]))) @ self.Gamma
        return self.A, self.B
