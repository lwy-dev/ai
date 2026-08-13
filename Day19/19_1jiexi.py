# 第1行
# import torch
# 导入 PyTorch。
# 相当于：
# import cv2
# 导入 OpenCV。
# 没有这行：
# torch.tensor()
# 就无法使用。
# ---
# 第2行
# from torchvision.models import resnet18
# 导入 ResNet18 模型。
# torchvision 是 PyTorch 官方视觉库。
# 里面有很多现成模型：
# ResNet18
# ResNet34
# ResNet50
# MobileNet
# VGG16
# 今天使用最简单的：
# ResNet18
# ---
# 创建 Tensor
# 第8行
# img = torch.randn(1, 3, 224, 224)
# 生成随机数字。
# ---
# randn()
# 意思：
# random normal
# 按照正态分布随机生成。
# 例如：
# torch.randn(3)
# 可能得到：
# tensor([0.21, -0.87, 1.32])
# ---
# 为什么是
# (1,3,224,224)
# 这是图片格式：
# (批量数, 通道数, 高度, 宽度)
# 即：
# 1张图片
# 3个颜色通道
# 224高
# 224宽
# 所以：
# 1
# ↓
# 3
# ↓
# 224
# ↓
# 224
# 代表：
# RGB图片
# ---
# 第10行
# print(img.shape)
# 查看张量形状。
# 输出：
# torch.Size([1, 3, 224, 224])
# 说明：
# 图片尺寸正确
# ---
# 加载模型
# 第18行
# model = resnet18(weights="DEFAULT")
# 加载预训练模型。
# 这里：
# weights="DEFAULT"
# 表示：
# 加载官方训练好的参数
# 不是空模型。
# 相当于：
# 直接使用已经学会识别图片的模型
# ---
# 如果写
# model = resnet18()
# 则：
# 随机参数
# 不会识别东西。
# ---
# 第20行
# print("模型加载成功")
# 验证模型已加载。
# ---
# 推理模式
# 第26行
# model.eval()
# 切换为推理模式。
# 训练模式：
# model.train()
# 预测模式：
# model.eval()
# ---
# 为什么需要？
# 因为很多层行为不同：
# 例如：
# Dropout
# BatchNorm
# 训练时：
# 随机丢弃神经元
# 预测时：
# 不能乱丢
# 所以：
# model.eval()
# 几乎是推理必写。
# ---
# 推理
# 第32行
# with torch.no_grad():
# 关闭梯度计算。
# ---
# 为什么？
# 训练需要：
# 记录梯度
# 计算反向传播
# 推理不需要。
# 所以关闭：
# 更快
# 更省内存
# ---
# 第33行
# output = model(img)
# 把图片送进模型。
# 流程：
# img
#  ↓
# ResNet18
#  ↓
# output
# ---
# 这里发生了什么？
# 实际上执行了：
# 卷积
# 池化
# 激活函数
# 全连接层
# 几十层神经网络计算。
# 最后输出结果。
# ---
# 查看结果
# 第40行
# print(output.shape)
# 输出：
# torch.Size([1,1000])
# 意思：
# 1张图片
# 1000个分类结果
# ---
# 为什么1000？
# 因为 ResNet18 在 ImageNet 上训练。
# ImageNet：
# 1000种物体
# 例如：
# 猫
# 狗
# 汽车
# 飞机
# 香蕉
# 苹果
# 椅子
# ...
# 共1000类。
# ---
# 第43行
# print(output[0][:10])
# 取：
# 第1张图片
# 前10个分类分数
# 例如：
# tensor([
#  0.21,
# -1.43,
#  2.34,
#  0.77,
#  ...
# ])
# ---
# 这些是什么？
# 叫：
# logits
# 即：
# 模型原始输出
# 不是概率。
# ---
# 如果想看概率
# 可以加：
# prob = torch.softmax(output, dim=1)
# print(prob[0][:10])
# ---
# softmax
# 作用：
# 把：
# 任意数字
# 变成：
# 0~1概率
# 例如：
# tensor([
# 0.02,
# 0.15,
# 0.70,
# 0.13
# ])
# 总和：
# 1
# ---
# Day19 你应该记住的重点
# torch.tensor()
# 创建张量
# ---
# torch.randn()
# 创建随机张量
# ---
# model = resnet18(weights="DEFAULT")
# 加载模型
# ---
# model.eval()
# 推理模式
# ---
# with torch.no_grad():
# 关闭梯度
# ---
# output = model(img)
# 执行推理
# ---
# output.shape
# 查看输出维度
# ---
# 如果你把这段代码跑通了，实际上就已经完成了 Day19 的“加载模型 + 模型推理成功”任务。接下来 Day20 学 YOLO 时，你会发现 YOLO 的推理流程和这里几乎一模一样：
# 读取图片
# ↓
# 转Tensor
# ↓
# 加载模型
# ↓
# model(img)
# ↓
# 得到结果
# 只是模型从 ResNet18 换成了 YOLO。