import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.models import load_model
import cv2
# 给数据类别放置到列表中
CLASS_NAMES = np.array(['Cr', 'In', 'Pa', 'PS', 'Rs', 'Sc'])
# 设置图片大小和批次数
IMG_HEIGHT = 32
IMG_WIDTH = 32
# 加载模型
model = load_model('model.keras')
# 读取图片
src = cv2.imread('./data/val/PS/PS_3.bmp')
# 将图片压缩
src = cv2.resize(src, (32,32))
# 转变图片数据类型
src = src.astype('int32')
# 图片大小归一化
src = src/255
# 单张图片为适用模型 应将其扩充维度
test_img = tf.expand_dims(src, 0)

# 预测结果
preds = model.predict(test_img)
# preds是二维列表 取出得分
score = preds[0]
print("模型预测结果为{}, 概率为{}".format(CLASS_NAMES[np.argmax(score)], np.max(score)))
