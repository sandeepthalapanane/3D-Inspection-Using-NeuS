import re
import matplotlib.pyplot as plt

# Open and read the text file
file_path = 'C:\\Users\\sande\\Documents\\3D_vision\\Project\\Final_results\\test_HFS_main\\exp\\scan106\\womask_hfs\\logs\\loss.txt'  # Replace with the actual path to your file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Parse iterations and losses from each line
iterations = []
losses = []

for line in lines:
    match = re.search(r'iter:(\d+) loss = ([\d.]+)', line)
    if match:
        iter_num = int(match.group(1))
        loss_val = float(match.group(2))
        iterations.append(iter_num)
        losses.append(loss_val)

# Plotting
plt.plot(iterations, losses, marker='o', linestyle='-', color='b')
plt.title('Iterations vs Loss')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.grid(True)
plt.show()
