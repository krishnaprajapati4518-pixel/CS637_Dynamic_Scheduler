def energy_consumption(P_static, T_HP, N_exec, E_exec, N_skip, E_skip):
    E_total = P_static * T_HP + N_exec * E_exec + N_skip * E_skip
    return E_total
