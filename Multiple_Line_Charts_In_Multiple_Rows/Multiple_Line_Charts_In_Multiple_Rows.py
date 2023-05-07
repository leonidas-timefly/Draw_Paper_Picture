import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_palette('deep')

fig, ax = plt.subplots(2, 2, figsize=(8, 6))

# Define data for subplots

data = [[[0.3538, 0.4096, 0.4336, 0.4654, 0.4743],
         [0.3320, 0.3943, 0.4135, 0.4636, 0.4731],
         [0.3073, 0.4092, 0.4258, 0.4473, 0.4636],
         [0.1092, 0.1035, 0.1288, 0.1527, 0.1072],
         [0.2970, 0.3386, 0.3748, 0.4091, 0.4201],
         [0.6360, 0.7019, 0.7912, 0.8002, 0.7941]],

        [[0.3421, 0.3891, 0.4577, 0.4606, 0.4791],
         [0.3509, 0.4197, 0.4242, 0.4430, 0.4938],
         [0.3364, 0.4105, 0.4277, 0.4497, 0.4818],
         [0.1355, 0.1811, 0.1460, 0.1527, 0.1380],
         [0.3016, 0.3587, 0.3931, 0.4035, 0.4288],
         [0.6755, 0.7162, 0.7364, 0.7806, 0.7951]],
         
        [[0.3547, 0.3910, 0.4035, 0.4781, 0.4807],
         [0.3088, 0.3922, 0.4206, 0.4331, 0.4434],
         [0.3483, 0.4019, 0.4393, 0.4484, 0.4781],
         [0.1343, 0.1431, 0.1384, 0.1577, 0.1581],
         [0.3253, 0.3515, 0.3916, 0.4106, 0.4244],
         [0.6518, 0.6930, 0.7628, 0.7827, 0.7979]],
         
        [[0.3554, 0.3956, 0.4042, 0.4575, 0.4634],
         [0.3534, 0.4004, 0.4202, 0.4505, 0.4417],
         [0.3606, 0.4063, 0.4191, 0.4563, 0.4630],
         [0.1485, 0.1305, 0.1947, 0.1628, 0.1378],
         [0.3051, 0.3612, 0.3729, 0.4007, 0.3990],
         [0.6377, 0.6910, 0.7384, 0.7811, 0.7852]],]

data = np.array(data)
x = list(range(0, 5))
values = ["1 K", "2 K", "3 K", "4 K", "5 K"]

#print(data[0,0].shape)
# Define markers for each line in each subplot
markers =['v', 'H', 'o', 'X', 'd', 's']

# Set common ylabel for all subplots
#fig.text(0.04, 0.5, 'Y-axis', ha='center', va='center', rotation='vertical')


plt.subplots_adjust(hspace=0.2)
title = ["VGGNet", "DenseNet", "ResNet", "MobileNet"]


for i in range(2):
    for j in range(2):
        # Plot lines with different markers
        ax[i, j].plot(x, data[i*2+j,0], marker=markers[0], markersize=6, color=sns.color_palette()[0], linewidth=2, label='Correia-Silva')
        ax[i, j].plot(x, data[i*2+j,1], marker=markers[1], markersize=6, color=sns.color_palette()[1], linewidth=2, label='Pal')
        ax[i, j].plot(x, data[i*2+j,2], marker=markers[2], markersize=6, color=sns.color_palette()[2], linewidth=2, label='Orekondy')
        ax[i, j].plot(x, data[i*2+j,3], marker=markers[3], markersize=6, color=sns.color_palette()[5], linewidth=2, label='Papernot')
        ax[i, j].plot(x, data[i*2+j,4], marker=markers[4], markersize=6, color=sns.color_palette()[4], linewidth=2, label='Yu')
        ax[i, j].plot(x, data[i*2+j,5], marker=markers[5], markersize=6, color=sns.color_palette()[3], linewidth=2, label='Ours')

        
        # Set subplot title and legend
        ax[i,j].set_ylim([0, 1])
        ax[i, j].set_title(title[i*2+j], fontsize=16)
        ax[i,j].set_ylabel('Fidelity', fontsize=16)
        ax[i,j].set_xticks(x, values)
        ax[i, j].legend()
        
# Adjust subplots layout
fig.tight_layout()

ax[0, 0].legend_.remove()
ax[0, 1].legend_.remove()
ax[1, 0].legend_.remove()
handles, labels = ax[1, 1].get_legend_handles_labels()
ax[1, 1].legend_.remove()

fig.legend(handles, labels, loc='lower center', ncol=6, bbox_to_anchor=[0.5, -0.04], frameon=True, fontsize=10)
plt.savefig('example2.pdf', dpi=200, bbox_inches='tight',pad_inches=0.1)
plt.show()
