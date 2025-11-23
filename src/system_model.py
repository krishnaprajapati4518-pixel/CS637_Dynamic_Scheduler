import numpy as np

class LTISystem:
    def __init__(self, Phi, Gamma, C, Q, R, gamma, safe_region):
        self.Phi = Phi
        self.Gamma = Gamma
        self.C = C
        self.Q = Q
        self.R = R
        self.gamma = gamma
        self.safe_region = safe_region

    def set_periods(self, periods):
        self.periods = periods
