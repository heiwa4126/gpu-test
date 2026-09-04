import torch

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))

# 出力例:
#  True
#  NVIDIA GeForce RTX 3070 Ti Laptop GPU
