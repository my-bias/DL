import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import keras
from keras.layers import Dense

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 导入数据
dataset = pd.read_csv('data.csv', encoding='utf-8')
dataset = np.array(dataset)
# 提取特征与标签
X = dataset[:, : -1]
Y = dataset[:, -1]
Y = np.reshape(Y, (len(Y), 1))
# 归一化数据
sc = MinMaxScaler()
X = sc.fit_transform(X)
Y = sc.fit_transform(Y)
# 划分数据集
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# 搭建神经网络模型
model = keras.Sequential()
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))
# 模型编译
model.compile(optimizer='SGD', loss='mse', metrics=['accuracy'])
# 模型训练
history = model.fit(x_train, y_train, batch_size=64, epochs=100, verbose=2, validation_data=(x_test, y_test))
model.save('model.keras')
# 绘制loss值图
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val')
plt.title("全连接神经网络loss值图")
plt.legend()
plt.show()
