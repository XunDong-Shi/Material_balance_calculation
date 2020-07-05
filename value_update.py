import gl


# 计算f7,f10,x7,x10的迭代值
def initial_value_update(init_array, iter_array):
    new_array = iter_array - (iter_array - init_array) / gl.Newton_iter_factor
    return new_array

