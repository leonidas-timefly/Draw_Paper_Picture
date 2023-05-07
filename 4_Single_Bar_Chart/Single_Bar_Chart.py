import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_palette('deep')
fig, ax = plt.subplots()

vgg11 = [0.8965, 0.8677, 0.8901, 0.7685]
vgg13 = [0.8429, 0.8525, 0.8853, 0.7676]
vgg16 = [0.8643, 0.9007, 0.8844, 0.7740]
vgg19 = [0.8227, 0.8389, 0.8780, 0.7608]
save_name = 'example'

labels = ['DenseNet121', 'ResNet50', 'VGGNet13', 'MobileNetV3']
x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars

rects1 = ax.bar(x - 3*width/4, vgg11, width/2, color=sns.color_palette()[0], label='VGGNet11')
rects2 = ax.bar(x - width/4, vgg13, width/2, color=sns.color_palette()[1], label='VGGNet13')
rects3 = ax.bar(x + width/4, vgg16, width/2, color=sns.color_palette()[2], label='VGGNet16')
rects4 = ax.bar(x + 3*width/4, vgg19, width/2, color=sns.color_palette()[3], label='VGGNet19')

ax.set_ylabel('Fidelity(%)', fontsize=16)
plt.ylim((0, 1))
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=16, rotation=20)


plt.yticks(fontsize=16)

ax.legend(loc=4, fontsize=16, frameon=True)

fig.tight_layout()
plt.savefig(save_name+'.png', dpi=200, bbox_inches='tight', pad_inches=0.1)
