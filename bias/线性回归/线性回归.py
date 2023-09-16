# 定义数据集
import math

import numpy as np

# 定义数据特征
x_data = np.array([1, 2, 3, 4, 5])
# 定义数据标签
y_data = np.array([2, 4, 6, 8, 10])

# 初始化参数W
w = 4


# 定义线性回归模型
def f(x):
    return x * w


# 定义损失函数
def loss(x, y):
    y_pred = f(x)
    loss_value = np.sum((y_pred - y) ** 2)
    return loss_value


# 定义计算梯度的函数
def gradient(x, y):
    grad = 2 * np.dot(x, (np.dot(x, w) - y))
    return grad


# 定义回归函数
def regression(x, y):
    global w
    count = 0
    error = loss(x, y)
    ETA = 0.001
    diff = 1
    while diff > 0.0001:
        count += 1
        grad_val = gradient(x, y)
        w = w - ETA * grad_val
        new_error = loss(x, y)
        diff = error - new_error
        error = new_error
        print(f"第{count}轮,w:{w},误差:{diff}")


if __name__ == '__main__':
    regression(x_data, y_data)
