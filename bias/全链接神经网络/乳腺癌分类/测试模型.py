import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import keras
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn.metrics import classification_report
from keras.models import load_model

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
x_test = sc.fit_transform(x_test)
# 将标签进行one--hot处理
y_test_one = to_categorical(y_test)

# 将训练好的模型导入
model = load_model('model.keras')

# 利用模型进行测试
predict = model.predict(x_test)
y_pred = np.argmax(predict, axis=1)

# 打印模型的精确的和召回率
report = classification_report(y_test, y_pred, labels=[0, 1], target_names=["良心", "恶性"])
print(report)
