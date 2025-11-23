class OnlineScheduler:
    def __init__(self, acess_lib, J_lb, J_ub):
        self.lib = acess_lib
        self.J_lb = J_lb
        self.J_ub = J_ub

    def update(self, J):
        if J >= self.J_ub:
            return "increase_util"
        elif J <= self.J_lb:
            return "decrease_util"
        else:
            return "maintain"
