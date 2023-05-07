import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_palette('deep')

fig, ax = plt.subplots(1, 4, figsize=(16, 3))

# Define data for subplots

data = [[[0.1882, 0.2235, 0.2824, 0.2882],
         [0.2118, 0.2765, 0.3294, 0.2879],
         [0.1765, 0.2787, 0.2588, 0.2647],
         [0.3353, 0.4529, 0.5000, 0.5000],],

        [[0.1652, 0.2757, 0.2937, 0.4211],
         [0.2951, 0.4227, 0.3993, 0.4547],
         [0.3429, 0.3511, 0.4274, 0.4721],
         [0.2412, 0.3854, 0.4470, 0.4655],],
         
        [[0.5210, 0.5360, 0.6570, 0.5340],
         [0.5200, 0.7495, 0.8445, 0.8660],
         [0.5165, 0.5195, 0.5875, 0.6140],
         [0.8405, 0.8985, 0.9150, 0.9425],],
         
        [[0.7646, 0.7850, 0.7862, 0.8034],
         [0.7846, 0.7744, 0.7990, 0.8016],
         [0.7402, 0.7404, 0.7402, 0.7738],
         [0.8342, 0.8378, 0.8408, 0.8510],],]

data = np.array(data)
x = np.arange(4)
values = [["0.50 K", "1.00 K", "1.50 K", "2.00 K"],
          ["1.00 K", "2.00 K", "3.00 K", "4.00 K"],
          ["0.36 K", "0.72 K", "1.08 K", "1.44 K"],
          ["0.24 K", "0.48 K", "0.72 K", "0.96 K"]]


# Set common ylabel for all subplots
#fig.text(0.04, 0.5, 'Y-axis', ha='center', va='center', rotation='vertical')

title = ["Flower Recognition API", "Traffic Recognition API", "NSFW Recognition API", "Moderation Recognition API"]

width = 0.4  # the width of the bars
for j in range(4):

        ax[j].bar(x - 3*width/4, data[j,0], width/2, color=sns.color_palette()[0], label='BAE')
        ax[j].bar(x - width/4, data[j,1], width/2, color=sns.color_palette()[1], label='DAE')
        ax[j].bar(x + width/4, data[j,2], width/2, color=sns.color_palette()[2], label='MoCo')
        ax[j].bar(x + 3*width/4, data[j,3], width/2, color=sns.color_palette()[3], label='SimCLR')

        ax[j].set_ylabel('Fidelity', fontsize=16)
        ax[j].set_ylim([0, 1])
        
        #ax[i,j].set_xticks(x, labels, fontsize=16)
        ax[j].set_xticks(x)
        ax[j].set_xticklabels(values[j], fontsize=12)

        #ax[i,j].set_yticks(fontsize=24)
        ax[j].set_title(title[j], fontsize=16)
        ax[j].legend()

# Adjust subplots layout
fig.tight_layout()

ax[0].legend_.remove()
ax[1].legend_.remove()
ax[2].legend_.remove()
handles, labels = ax[3].get_legend_handles_labels()
ax[3].legend_.remove()

fig.legend(handles, labels, loc='lower center', ncol=4, bbox_to_anchor=[0.5, -0.14], frameon=True, fontsize=16)
plt.savefig('example.pdf', dpi=200, bbox_inches='tight',pad_inches=0.1)
plt.show()
