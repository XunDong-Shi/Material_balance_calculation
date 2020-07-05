import gl


def separation(x, phase_equilibrium_const, phase_ratio_init, max_inter=10000):
    for i in range(0, max_inter):
        f = df = 0
        for j in range(0, 5):
            f = f + x[j] * (1 - phase_equilibrium_const[j]) / (phase_ratio_init + phase_equilibrium_const[j])
            df = df - x[j] * (1 - phase_equilibrium_const[j]) / ((phase_ratio_init + phase_equilibrium_const[j]) ** 2)
        phase_ratio_iter = phase_ratio_init - f / df
        if abs((phase_ratio_iter - phase_ratio_init) / phase_ratio_init) <= gl.Iteration_acc:
            return phase_ratio_iter
        else:
            phase_ratio_init = phase_ratio_iter
    print(u"已达到最大迭代次数，但是仍然无法收敛")
