import torch
import numpy as np

# # Initiating a tensor directly from data
# data = [[1, 2], [3, 4]]
# x_data = torch.tensor(data)
# print(x_data)

# # Initiating a tensor from a NumPy array
# np_array = np.array(data)
# x_np = torch.from_numpy(np_array)
# print(x_np)

# Artribute of a Tensor
tensor = torch.rand(3, 4)
print(f"Shape of tensor: {tensor.shape}")
print(f"Datatype of tensor: {tensor.dtype}")
print(f"Device tensor is stored on: {tensor.device}")
print(f"Layout of tensor: {tensor.layout}")
print(f"Values of tensor: \n{tensor}")
print(f"First row of tensor: {tensor[0]}")
print(f"First column of tensor: {tensor[:, 0]}")
print(f"Last column of tensor: {tensor[..., -1]}")

