import numpy as np
from scipy.linalg import expm

class SubsystemGenerator:
    def __init__(self, system, max_skips=3):
        self.sys = system
        self.max_skips = max_skips

    def discretize(self, h):
        A = expm(self.sys.Phi * h)
        B = np.dot(np.linalg.inv(self.sys.Phi), (A - np.eye(len(A)))) @ self.sys.Gamma
        return A, B

    def generate_subsystems(self):
        subsystems = []
        for h in self.sys.periods:
            A, B = self.discretize(h)

            for i in range(self.max_skips + 1):
                if i == 0:
                    A_mode = A
                else:
                    A_mode = np.block([
                        [A - B * 0, np.zeros_like(B)],
                        [np.zeros_like(B.T), np.eye(len(A))]
                    ])

                subsystems.append({
                    "period": h,
                    "skips": i,
                    "A": A_mode
                })

        return subsystems
