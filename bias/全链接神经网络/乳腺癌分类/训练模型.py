import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import keras
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.metrics import classification_report

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 导入数据
dataset = pd.read_csv('breast_cancer_data.csv', encoding='utf-8')
# 提取数据与标签
X = dataset.iloc[:, :-1]
Y = dataset['target']
# 划分数据集
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# 将数据归一化处理
sc = MinMaxScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
# 将标签进行one--hot处理
y_train_one = to_categorical(y_train)
y_test_one = to_categorical(y_test)

# 利用keras框架搭建神经网络模型
model = keras.Sequential()
model.add(Dense(10, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(2, activation='softmax'))

# 对神经网络模型进行编译
model.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])

# 对模型进行训练
history = model.fit(x_train, y_train_one, epochs=120, batch_size=32, verbose=2, validation_data=(x_test, y_test_one))
model.save('model.keras')

# 绘制loss值图
plt.plot(history.history['loss'], label='train')
plt.plot(history.history['val_loss'], label='val')
plt.title("全连接神经网络loss值图")
plt.legend()
plt.show()

# 绘制accuracy值图
plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='val')
plt.title("全连接神经网络accuracy值图")
plt.legend()
plt.show()
