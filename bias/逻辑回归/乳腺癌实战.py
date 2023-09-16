import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# 读取数据
data_set = pd.read_csv('breast_cancer_data.csv')
# 提取X
X = data_set.iloc[:, : -1]
# 提取Y
Y = data_set['target']
# 划分训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
# 进行数据的归一化处理
sc = MinMaxScaler(feature_range=(0, 1))
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
# 搭建逻辑回归的模型
lr = LogisticRegression()
lr.fit(x_train,y_train)
# 打印模型参数 coef_:系数 intercept_:截距
print("w:", lr.coef_)
print("b:", lr.intercept_)
# 利用训练好的模型进行数据预测
pre_result = lr.predict(x_test)
# 预测结果的概率
pre_result_pro = lr.predict_proba(x_test)
# 设置阙值
threshold = 0.30

# 获取恶性肿瘤的概率
result = pre_result_pro[:, 1]
for ind,val in enumerate(result):
    if val > threshold:
        result[ind] = 1
    else:
        result[ind] = 0

report = classification_report(y_test,result,labels=(0,1), target_names=['良性','恶性'])
print(report)
"""
w: [[ 1.7153642   1.54879644  1.69791438  1.46350043  0.64456298  0.40474274
   1.3987998   2.00857374  0.38979999 -0.92136439  1.17940917  0.08746075
   0.9311738   0.77879709  0.08702191 -0.51160467 -0.22105135  0.30297161
  -0.40213381 -0.56206807  2.1825632   2.10193661  2.03321962  1.58416155
   1.32871775  0.76738196  1.24244213  2.49341322  1.19471461  0.36819989]]
b: [-8.50894771]
          良性       1.00      0.96      0.98        70
          恶性       0.94      1.00      0.97        44
"""