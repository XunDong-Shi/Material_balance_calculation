from value_update import initial_value_update
import gl
from Chemical_Process import main_process
import time
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def main(emission_ratio):
    init_array, iter_array, error_array, flow, fraction = main_process(gl.init_F7, gl.init_F10, gl.init_X7, gl.init_X10,
                                                                       emission_ratio)
    i = 0
    for j in range(0, 4):
        while (error_array[j] > gl.Iteration_acc).any():
            new_array = initial_value_update(init_array, iter_array)
            init_array, iter_array, error, flow, fraction = main_process(new_array[0], new_array[1],
                                                                         new_array[2], new_array[3],
                                                                         emission_ratio)
            error_array[j] = error[j]
            i += 1
            time.sleep(0.01)

    # 将计算结果输出
    df_flow = pd.DataFrame(flow, index=range(1, 11), columns=["摩尔流量"])
    df_fraction = pd.DataFrame(fraction, index=range(1, 11), columns=["摩尔分率N2", "摩尔分率H2", "摩尔分率NH3",
                                                                      "摩尔分率Ar", "摩尔分率CH4"])
    df_output = pd.concat([df_flow, df_fraction], axis=1).round(4)
    return df_output
    print("共经{}次迭代，完成物料平衡计算,输出结果如下：".format(i))
    print(df_output)


if __name__ == '__main__':
    emission_ratio_list = np.arange(0.02, 0.11, 0.005)
    NH3_production_list = []
    for emission_ratio in emission_ratio_list:
        NH3_production_list.append(main(emission_ratio)["摩尔流量"][10])
    df_plot = pd.DataFrame({"emission_ratio": emission_ratio_list, "NH3_production": NH3_production_list})
    sns.lineplot(x="emission_ratio", y="NH3_production", data=df_plot)
    plt.show()

