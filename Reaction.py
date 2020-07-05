import gl


# 根据n43、n3、f3值计算出函数关系func的值
def func_value(n43_init, n3, f3):
    n41 = (2 * n3[0] + n3[2] - n43_init) / 2
    n42 = (2 * n3[1] + 3 * n3[2] - 3 * n43_init) / 2
    f4 = f3 + n3[2] - n43_init
    value = n43_init ** 2 / (n41 * n42 ** 3) - gl.Chem_reac_equ_const / f4 ** 2
    return value


# 根据n43初值、n3和f3的值计算出n43迭代值和迭代误差
def react_calculation(n43_init, n3, f3):
    f_reaction_1 = func_value(n43_init, n3, f3)
    n43_2 = n43_init + gl.Step
    f_reaction_2 = func_value(n43_2, n3, f3)
    fd = (f_reaction_2 - f_reaction_1) / gl.Step
    n43_iteration = n43_init - f_reaction_1 / fd
    delta = abs((n43_iteration - n43_init) / n43_init)
    return n43_iteration, delta


# 根据n43，n3和f3计算出n43最终解
def react_model(n43_init, n3, f3):
    n43_iteration, delta = react_calculation(n43_init, n3, f3)
    while delta >= gl.Iteration_acc:
        n43_init = n43_iteration
        n43_iteration, delta = react_calculation(n43_init, n3, f3)
    return n43_iteration
