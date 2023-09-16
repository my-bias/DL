import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 导入数据集
dataset = pd.read_csv('LBMA-GOLD.csv', index_col=[0])
# 设置训练集长度
train_len = int(len(dataset) * 0.8)
test_set = dataset.iloc[train_len:, [0]]
print(test_set)
# 数据归一化
sc = MinMaxScaler(feature_range=(0, 1))
test_set = sc.fit_transform(test_set)
# 设置测试集特征和标签
x_test = []
y_test = []
# 设置周期T
T = 5
for i in range(T, len(test_set)):
    x_test.append(test_set[i - T:i, 0])
    y_test.append(test_set[i, 0])
print(x_test)
# 转换格式
x_test, y_test = np.array(x_test), np.array(y_test)
# 循环神经网络的特征格式为[样本数, 时间步, 特征个数]
x_test = np.reshape(x_test, (x_test.shape[0], T, 1))

# 导入模型
model = load_model('model.keras')
predict = model.predict(x_test)
predict = sc.inverse_transform(predict)
real = y_test
real = np.reshape(real, (len(real), 1))
real = sc.inverse_transform(real)
# 计算评价指标
rmse = np.sqrt(mean_squared_error(real, predict))
mape = np.mean(np.abs(predict - real) / predict)
print('rmse:', rmse)
print('mape:', mape)
plt.plot(predict,label='pre')
plt.plot(real,label='real')
plt.title('LSTM预测值与真实值对比图')
plt.legend()
plt.show()
