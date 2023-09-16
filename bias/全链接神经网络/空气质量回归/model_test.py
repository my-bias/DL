import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.models import load_model
from numpy import concatenate
from sklearn.metrics import mean_squared_error

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 导入数据
dataset = pd.read_csv('data.csv', encoding='utf-8')
# 归一化数据
sc = MinMaxScaler(feature_range=(0, 1))
scaled = sc.fit_transform(dataset)
dataset_sc = pd.DataFrame(scaled)

# 提取特征与标签
X = dataset_sc.iloc[:, : -1]
Y = dataset_sc.iloc[:, -1]

# 划分数据集
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 加载模型
model = load_model('model.keras')
# 模型预测
yhat = model.predict(x_test)

# 进行预测值反归一化
inv_yhat = concatenate((x_test, yhat), axis=1)
inv_yhat = sc.inverse_transform(inv_yhat)
prediction = inv_yhat[:, -1]

# 将y_test维度转换
y_test = np.array(y_test)
y_test = np.reshape(y_test, (y_test.shape[0], 1))

# 反向缩放真实值
inv_y = concatenate((x_test, y_test), axis=1)
inv_y = sc.inverse_transform(inv_y)
real = inv_y[:, -1]
print(real)
# 计算评价指标
rmse = np.sqrt(mean_squared_error(real, prediction))
mape = np.mean(np.abs((real - prediction) / prediction))
# 打印rmse,mape
print(rmse)
print(mape)

# 画出真实值与预测值的对比图
plt.plot(prediction, label='预测值')
plt.plot(real, label='真实值')
plt.title("全连接神经网络空气质量对比图")
plt.legend()
plt.show()
