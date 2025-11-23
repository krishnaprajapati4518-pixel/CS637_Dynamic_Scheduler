import cvxpy as cp
import numpy as np

class StabilityAnalyzer:
    def __init__(self, decay_rate):
        self.gamma = decay_rate

    def check_stability(self, A):
        n = A.shape[0]
        P = cp.Variable((n, n), symmetric=True)

        constraint = A.T @ P @ A - (1 + self.gamma) * P << 0
        constraints = [P >> 1e-6 * np.eye(n), constraint]

        prob = cp.Problem(cp.Minimize(0), constraints)
        result = prob.solve(solver=cp.SCS)

        if prob.status == cp.OPTIMAL:
            return True, P.value
        return False, None
