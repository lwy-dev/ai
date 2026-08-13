from PIL import Image
from torchvision import transforms
from torchvision.models import resnet18

import torch

# 加载图片
img = Image.open("person.jpg").convert("RGB")

# 转Tensor
transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

img = transform(img)

# 增加Batch维度
img = img.unsqueeze(0)

# 加载模型
model = resnet18(weights="DEFAULT")
model.eval()

# 推理
with torch.no_grad():
    output = model(img)

print(output.shape)
