from PIL import Image
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights
import torch

# 权重
weights = ResNet18_Weights.DEFAULT

# 图片
img = Image.open("person.jpg").convert("RGB")

# 官方预处理
transform = weights.transforms()

img = transform(img)
img = img.unsqueeze(0)

# 模型
model = resnet18(weights=weights)
model.eval()

# 推理
with torch.no_grad():
    output = model(img)

# 找最大值下标
pred = output.argmax(dim=1).item()

# 类别名称
categories = weights.meta["categories"]

print("类别编号：", pred)
print("类别名称：", categories[pred])