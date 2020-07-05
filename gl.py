import numpy as np

# 高压分离器中组分的气液平衡常数
Hps_Gle_Const = np.array([105, 90, 0.06, 100, 33])

# 低压分离器中组分的气液平衡常数
Lps_Cle_Const = np.array([2400, 1750, 0.28, 1400, 500])

# 入料分子流量
Mol_flow_f1 = 100

# 原料组成（摩尔分率）
Mol_fraction_x1 = np.array([0.24, 0.743, 0, 0.006, 0.011])

# 组分相对分子质量
Molecular_mass = np.array([28, 2, 17, 40, 16])

# 化学平衡常数
Chem_reac_equ_const = 0.35

# 迭代精度
Iteration_acc = 1e-4

# 斜率计算步长
Step = 1e-4

# 牛顿迭代阻尼因子
Newton_iter_factor = 5

# 剥离变量初始值
init_F7 = init_F10 = 100
init_X7 = init_X10 = np.array([0.25, 0.75, 0, 0, 0])
init_N43 = 50
