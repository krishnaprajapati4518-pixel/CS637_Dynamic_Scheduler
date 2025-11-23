from sortedcontainers import SortedDict

class OnlineScheduler:
    def __init__(self):
        self.task_libraries = {}
        self.cost_bounds = {}

    def add_task(self, task_name, M, J_lb, J_ub):
        self.task_libraries[task_name] = SortedDict(M)
        self.cost_bounds[task_name] = (J_lb, J_ub)

    def run(self, task_costs):
        for task, J in task_costs.items():
            M = self.task_libraries[task]
            J_lb, J_ub = self.cost_bounds[task]

            if J >= J_ub:
                print(f"{task}: increase utilization (select higher-frequency ACESS)")
            elif J <= J_lb:
                print(f"{task}: decrease utilization (select lower-frequency ACESS)")
