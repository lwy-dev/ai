import torch
from torchvision.models import resnet18

# ======================
# 1. 创建Tensor
# ======================

img = torch.randn(1, 3, 224, 224)

print("输入图片形状：")
print(img.shape)

# ======================
# 2. 加载模型
# ======================

model = resnet18(weights="DEFAULT")

print("\n模型加载成功")

# ======================
# 3. 切换到推理模式
# ======================

model.eval()

# ======================
# 4. 模型推理
# ======================

with torch.no_grad():
    output = model(img)

# ======================
# 5. 查看结果
# ======================

print("\n输出结果形状：")
print(output.shape)

print("\n前10个输出值：")
print(output[0][:10])
