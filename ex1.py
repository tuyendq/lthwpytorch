import torch

# z = torch.zeros(5,3)
# print(z)
# print(z.dtype)

# i = torch.ones((5,3), dtype=torch.int16)
# print(i)

torch.manual_seed(1729)
r1 = torch.rand(2, 2)
print('A random tensor:')
print(r1)

r2 = torch.rand(2, 2)
print('\nA different random tensor:')
print(r2)  # new values

torch.manual_seed(1729)
r3 = torch.rand(2, 2)
print('\nShould match r1:')
print(r3)  # repeats values of r1


