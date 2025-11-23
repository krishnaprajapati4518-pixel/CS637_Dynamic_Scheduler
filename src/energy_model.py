class EnergyModel:
    def __init__(self, P_static, E_exec, E_skip):
        self.P_static = P_static
        self.E_exec = E_exec
        self.E_skip = E_skip

    def compute(self, T_HP, N_exec, N_skip):
        return self.P_static * T_HP + N_exec * self.E_exec + N_skip * self.E_skip
