import numpy as np
import gl
from Separation import separation
from Reaction import react_model


def main_process(f7_init, f10_init, x7_init, x10_init, emi_fraction_const=0.02):
    # 依据设计输入值和初值计算物流1、7、10的摩尔流量
    n1 = gl.Mol_flow_f1 * gl.Mol_fraction_x1
    n7 = f7_init * x7_init
    n10 = f10_init * x10_init

    # 求解低压混合器出口物流2的总流量、摩尔流量、组分构成
    f2 = gl.Mol_flow_f1 + f7_init
    n2 = n1 + n7
    x2 = n2 / f2

    # 求解高压混合器出口物流3的总流量、摩尔流量、组分构成
    f3 = f2 + f10_init
    n3 = n2 + n10
    x3 = n3 / f3

    # 求解反应器出口物流4的总流量、摩尔流量、组分构成
    n4 = np.empty([5, ])
    n43_iteration = react_model(gl.init_N43, n3, f3)
    n4[2] = n43_iteration
    n4[3] = n3[3]
    n4[4] = n3[4]
    n4[0] = (2 * n3[0] + n3[2] - n4[2]) / 2
    n4[1] = (2 * n3[1] + 3 * n3[2] - 3 * n4[2]) / 2
    f4 = n4.sum()
    x4 = n4 / f4

    # 求解高压分离器出口产品的液/气相比例
    a1 = separation(x4, gl.Hps_Gle_Const, 0.15)

    # 依据液气相比例求解高压分离器出口物流5、物流8的组成和流量
    f8 = f4 / (1 + a1)
    f5 = a1 * f8
    x5 = f4 * x4 / (f8 * (a1 + gl.Hps_Gle_Const))
    x8 = gl.Hps_Gle_Const * x5

    # 依据排放率求解物流分解器出口物流9、物流10的组成和流量
    f9 = emi_fraction_const * f8
    f10_iter = f8 - f9
    x9 = x10_iter = x8

    # 求解低压分离器出口产品的液/气相比例
    a2 = separation(x5, gl.Lps_Cle_Const, 10)

    # 依据液气相比例求解高压分离器出口物流6、物流7的组成和流量
    f7_iter = f5 / (1 + a2)
    f6 = f5 - f7_iter
    x6 = f5 * x5 / (f7_iter * (a2 + gl.Lps_Cle_Const))
    x7_iter = gl.Lps_Cle_Const * x6

    # 返回计算过程的初值、迭代值、迭代误差、物流流量和组分构成
    init_array = np.array([f7_init, f10_init, x7_init, x10_init])
    iter_array = np.array([f7_iter, f10_iter, x7_iter, x10_iter])
    error_array = abs((iter_array - init_array) / init_array)
    mol_flow = np.array([gl.Mol_flow_f1, f2, f3, f4, f5, f6, f7_iter, f8, f9, f10_iter])
    mol_fraction = np.array([gl.Mol_fraction_x1, x2, x3, x4, x5, x6, x7_iter, x8, x9, x10_iter])
    return init_array, iter_array, error_array, mol_flow, mol_fraction

