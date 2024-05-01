import torch

tensor_dataset = torch.zeros((1, 1), dtype=torch.long)
print(tensor_dataset)

with open('text.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())
