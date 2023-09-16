import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 导入数据集
dataset = pd.read_csv('LBMA-GOLD.csv', index_col=[0])
print(dataset)
# 设置训练集长度
train_len = int(len(dataset) * 0.8)
# 划分训练集和测试集
train_set = dataset.iloc[:train_len, [0]]
test_set = dataset.iloc[train_len:, [0]]
# 数据归一化
sc = MinMaxScaler(feature_range=(0, 1))
train_set = sc.fit_transform(train_set)
test_set = sc.fit_transform(test_set)
# 设置训练集特征和标签
x_train = []
y_train = []
# 设置测试集特征和标签
x_test = []
y_test = []
# 设置周期T
T = 5
# 利用for循环进行特征和标签的设置
for i in range(T, len(train_set)):
    x_train.append(train_set[i - T:i, 0])
    y_train.append(train_set[i, 0])
for i in range(T, len(test_set)):
    x_test.append(test_set[i - T:i, 0])
    y_test.append(test_set[i, 0])
# 转换格式
x_train, y_train = np.array(x_train), np.array(y_train)
x_test, y_test = np.array(x_test), np.array(y_test)
# 循环神经网络的特征格式为[样本数, 时间步, 特征个数]
x_train = np.reshape(x_train, (x_train.shape[0], T, 1))
x_test = np.reshape(x_test, (x_test.shape[0], T, 1))

# 搭建LSTM模型
model = keras.Sequential()
model.add(LSTM(80, return_sequences=True, activation='relu'))
model.add(LSTM(80, return_sequences=False, activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense((1)))
# 编译
model.compile(loss='mse' ,optimizer='Adam')
# 训练
history = model.fit(x_train,y_train,batch_size=64, epochs=100,validation_data=(x_test,y_test))
model.save('model.keras')
# loss值可视化
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val')
plt.legend()
plt.show()
