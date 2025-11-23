import cvxpy as cp
import numpy as np

def check_LMI(Aq, Pq):
    '''Solve LMI: Aᵀ P A - P ≤ 0'''
    P = cp.Variable(Pq.shape, symmetric=True)
    constraint = Aq.T @ P @ Aq - P << 0
    prob = cp.Problem(cp.Minimize(0), [constraint, P >> np.eye(Pq.shape[0])])
    prob.solve(solver=cp.SCS)
    return P.value, prob.status
