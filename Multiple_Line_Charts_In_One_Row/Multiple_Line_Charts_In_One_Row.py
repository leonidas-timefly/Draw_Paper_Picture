import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_palette('deep')

fig, ax = plt.subplots(1, 4, figsize=(20, 4))

# Define data for subplots

data = [[[0.1725, 0.2000, 0.2235, 0.3059, 0.3471],
         [0.1412, 0.2353, 0.2824, 0.3118, 0.3235],
         [0.1647, 0.1765, 0.1529, 0.1765, 0.1471],
         [0.1176, 0.0941, 0.1294, 0.1118, 0.1176],
         [0.1941, 0.1941, 0.1882, 0.2059, 0.2471],
         [0.3353, 0.4529, 0.5000, 0.5000, 0.4941]],

        [[0.2785, 0.3429, 0.3844, 0.4184, 0.4251],
         [0.2308, 0.3461, 0.4167, 0.4169, 0.4538],
         [0.2248, 0.2945, 0.3373, 0.3869, 0.3779],
         [0.1187, 0.1256, 0.0940, 0.1551, 0.1448],
         [0.1631, 0.2292, 0.2710, 0.2711, 0.2643],
         [0.2412, 0.3854, 0.4470, 0.4655, 0.5124]],
         

        [[0.4850, 0.5085, 0.5025, 0.5020, 0.5250],
         [0.5155, 0.5220, 0.5100, 0.5210, 0.5210],
         [0.5025, 0.5135, 0.5090, 0.5120, 0.5160],
         [0.5145, 0.5185, 0.4650, 0.4690, 0.5210],
         [0.5235, 0.5215, 0.5080, 0.5210, 0.5105],
         [0.8405, 0.8985, 0.9150, 0.9425, 0.9510]],
         

        [[0.7268, 0.7622, 0.7866, 0.7974, 0.8092],
         [0.7394, 0.7742, 0.8142, 0.8006, 0.8100],
         [0.7396, 0.7736, 0.8142, 0.8016, 0.8238],
         [0.6692, 0.7194, 0.6446, 0.6776, 0.7028],
         [0.7284, 0.7352, 0.7500, 0.7764, 0.7730],
         [0.8342, 0.8378, 0.8408, 0.8510, 0.8470]],]

data = np.array(data)
x = list(range(0, 5))
values = [["0.50 K", "1.00 K", "1.50 K", "2.00 K", "2.50 K"],
          ["1.00 K", "2.00 K", "3.00 K", "4.00 K", "5.00 K"],
          ["0.36 K", "0.72 K", "1.08 K", "1.44 K", "1.80 K"],
          ["0.24 K", "0.48 K", "0.72 K", "0.96 K", "1.20 K"]]

#print(data[0,0].shape)
# Define markers for each line in each subplot
markers =['v', 'H', 'o', 'X', 'd', 's']

# Set common ylabel for all subplots
#fig.text(0.04, 0.5, 'Y-axis', ha='center', va='center', rotation='vertical')


plt.subplots_adjust(hspace=0.2)
title = ["Flower Recognition API", "Traffic Recognition API", "NSFW Recognition API", "Moderation Recognition API"]


for j in range(4):

    # Plot lines with different markers
    ax[j].plot(x, data[j,0], marker=markers[0], markersize=6, color=sns.color_palette()[0], linewidth=2, label='Correia-Silva')
    ax[j].plot(x, data[j,1], marker=markers[1], markersize=6, color=sns.color_palette()[1], linewidth=2, label='Pal')
    ax[j].plot(x, data[j,2], marker=markers[2], markersize=6, color=sns.color_palette()[2], linewidth=2, label='Orekondy')
    ax[j].plot(x, data[j,3], marker=markers[3], markersize=6, color=sns.color_palette()[5], linewidth=2, label='Papernot')
    ax[j].plot(x, data[j,4], marker=markers[4], markersize=6, color=sns.color_palette()[4], linewidth=2, label='Yu')
    ax[j].plot(x, data[j,5], marker=markers[5], markersize=6, color=sns.color_palette()[3], linewidth=2, label='Ours')

    
    # Set subplot title and legend
    ax[j].set_ylim([0, 1])

    ax[j].tick_params(axis='y', labelsize=12)

    ax[j].set_title(title[j], fontsize=16)
    ax[j].set_ylabel('Fidelity', fontsize=16)
    ax[j].set_xticks(x, values[j], fontsize=12)
    ax[j].legend()
        
# Adjust subplots layout
fig.tight_layout()

ax[0].legend_.remove()
ax[1].legend_.remove()
ax[2].legend_.remove()
handles, labels = ax[3].get_legend_handles_labels()
ax[3].legend_.remove()

fig.legend(handles, labels, loc='lower center', ncol=6, bbox_to_anchor=[0.5, -0.1], frameon=True, fontsize=16)
plt.savefig('comAPI.pdf', dpi=200, bbox_inches='tight',pad_inches=0.1)
plt.show()
