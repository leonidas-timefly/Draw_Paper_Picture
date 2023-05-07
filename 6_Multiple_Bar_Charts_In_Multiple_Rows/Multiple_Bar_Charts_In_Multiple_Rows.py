import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_palette('deep')

fig, ax = plt.subplots(2, 4, figsize=(20, 8))

# Define data for subplots

data = [[[0.3510, 0.4127, 0.4750, 0.5172],
         [0.3813, 0.4502, 0.4435, 0.4957],
         [0.7175, 0.7640, 0.8096, 0.8205],
         [0.6360, 0.7019, 0.7912, 0.8002]],

        [[0.3874, 0.3422, 0.4515, 0.5079],
         [0.3135, 0.4139, 0.4298, 0.4937],
         [0.6964, 0.7576, 0.8065, 0.8197],
         [0.6755, 0.7162, 0.7364, 0.7806]],

        [[0.3669, 0.4449, 0.4785, 0.5075],
         [0.3063, 0.3624, 0.4853, 0.4922],
         [0.7213, 0.7685, 0.7887, 0.8142],
         [0.6518, 0.6930, 0.7628, 0.7827]],
         
        [[0.3328, 0.4327, 0.4914, 0.4895],
         [0.3145, 0.3607, 0.4704, 0.4995],
         [0.6835, 0.7772, 0.8017, 0.8101],
         [0.6377, 0.6910, 0.7384, 0.7811]],


         [[0.3345, 0.3680, 0.4158, 0.4263],
         [0.3364, 0.3822, 0.4259, 0.4600],
         [0.6269, 0.7448, 0.7861, 0.8194],
         [0.5164, 0.6239, 0.6821, 0.7185]],

        [[0.2756, 0.3528, 0.4161, 0.4301],
         [0.3063, 0.3688, 0.3961, 0.4412],
         [0.7264, 0.7748, 0.8027, 0.8146],
         [0.5581, 0.5936, 0.6945, 0.6894]],
         
        [[0.2814, 0.3435, 0.3991, 0.4131],
         [0.2956, 0.3471, 0.4224, 0.4169],
         [0.6839, 0.7134, 0.8040, 0.8021],
         [0.4918, 0.6415, 0.6416, 0.6814]],
         
        [[0.3074, 0.3686, 0.4174, 0.4261],
         [0.3111, 0.3896, 0.4289, 0.4809],
         [0.6565, 0.7104, 0.7256, 0.7556],
         [0.4968, 0.5080, 0.5921, 0.5940]]]

data = np.array(data)
labels = ['Budget A', 'Budget B', 'Budget C', 'Budget D']
x = np.arange(len(labels))



plt.subplots_adjust(hspace=0.2)
title = ["VGGNet", "DenseNet", "ResNet", "MobileNet"]

width = 0.4  # the width of the bars
for i in range(2):
    for j in range(4):
        # Plot lines with different markers
        
        ax[i, j].bar(x - 3*width/4, data[i*4+j,0], width/2, color=sns.color_palette()[0], label='BAE')
        ax[i, j].bar(x - width/4, data[i*4+j,1], width/2, color=sns.color_palette()[1], label='DAE')
        ax[i, j].bar(x + width/4, data[i*4+j,2], width/2, color=sns.color_palette()[2], label='MoCo')
        ax[i, j].bar(x + 3*width/4, data[i*4+j,3], width/2, color=sns.color_palette()[3], label='SimCLR')

        ax[i,j].set_ylabel('Fidelity', fontsize=16)
        ax[i,j].set_ylim([0, 1])

        #ax[i,j].set_xticks(x, labels, fontsize=16)
        ax[i,j].set_xticks(x)
        ax[i,j].set_xticklabels(labels, fontsize=12)

        #ax[i,j].set_yticks(fontsize=24)
        ax[i, j].set_title(title[j], fontsize=16)
        ax[i, j].legend()
        if i == 0 and j == 0: # first row
            ax[i, j].text(-0.15, 0.5, 'CIFAR10', transform=ax[i, j].transAxes, fontsize=16, ha='right', va='center', rotation=90)
        if i == 1 and j == 0: # first row
            ax[i, j].text(-0.15, 0.5, 'STL10', transform=ax[i, j].transAxes, fontsize=16, ha='right', va='center', rotation=90)
# Adjust subplots layout
fig.tight_layout()

ax[0, 0].legend_.remove()
ax[0, 1].legend_.remove()
ax[0, 2].legend_.remove()
ax[0, 3].legend_.remove()
ax[1, 0].legend_.remove()
ax[1, 1].legend_.remove()
ax[1, 2].legend_.remove()
handles, labels = ax[1, 3].get_legend_handles_labels()
ax[1, 3].legend_.remove()

fig.legend(handles, labels, loc='lower center', ncol=4, bbox_to_anchor=[0.5, -0.08], frameon=True, fontsize=16)
plt.savefig('example3.pdf', dpi=200, bbox_inches='tight',pad_inches=0.1)
plt.show()

