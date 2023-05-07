import sys
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
sns.set_palette('deep')
fig = plt.plot(figsize=(8, 6))


choice = "stl10"
if choice == "cifar10":
    fid_PriorMS = [0.4269, 0.8270, 0.8835, 0.8932, 0.8966, 0.8979, 0.8988, 0.8993]
    fid_Copycat = [0.1776, 0.5679, 0.7840, 0.8594, 0.8869, 0.8949, 0.8978, 0.8989]
    fid_ActiveThief = [0.1806, 0.5603, 0.7701, 0.8510, 0.8801, 0.8929, 0.8971, 0.8985]
    fid_KnockOff = [0.1764, 0.5609, 0.7711, 0.8513, 0.8807, 0.8919, 0.8961, 0.8980]
    fid_JBDA = [0.1661, 0.5431, 0.7669, 0.8502, 0.8834, 0.8932, 0.8972, 0.8986]
    fid_CloudLeak = [0.1821, 0.5725, 0.7833, 0.8576, 0.8852, 0.8936, 0.8975, 0.8989]
    save_name = "ae_"+choice

elif choice == "stl10":
    fid_PriorMS = [0.1239, 0.3202, 0.5301, 0.6726, 0.7516, 0.7954, 0.8223, 0.8390]
    fid_Copycat = [0.0723, 0.1777, 0.3372, 0.5067, 0.6460, 0.7418, 0.7949, 0.8289]
    fid_ActiveThief = [0.0711, 0.1749, 0.3270, 0.4801, 0.6101, 0.6988, 0.7557, 0.7903]
    fid_KnockOff = [0.0713, 0.1794, 0.3403, 0.5073, 0.6360, 0.7199, 0.7753, 0.8039]
    fid_JBDA = [0.0712, 0.1811, 0.3465, 0.5158, 0.6525, 0.7436, 0.7966, 0.8266]
    fid_CloudLeak = [0.0703, 0.1721, 0.3266, 0.4918, 0.6150, 0.7089, 0.7689, 0.7993]
    save_name = "ae_"+choice

values = ["0.03", "0.06", "0.09", "0.12", "0.15", "0.18", "0.21", "0.24"]
x_axis = list(range(0, len(fid_Copycat)))

#0.84
if choice == "cifar10":
    plt.axhline(y=0.90, linestyle='--', color='gray')
elif choice == "stl10":
    plt.axhline(y=0.84, linestyle='--', color='gray')
plt.plot(x_axis, fid_Copycat, marker='v',markersize=8, color=sns.color_palette()[0], linewidth=4, label='Correia-Silva')
plt.plot(x_axis, fid_ActiveThief, marker='H',markersize=8, color=sns.color_palette()[1], linewidth=4, label='Pal')
plt.plot(x_axis, fid_KnockOff, marker='o',markersize=8, color=sns.color_palette()[2], linewidth=4, label='Orekondy')
plt.plot(x_axis, fid_JBDA, marker='d',markersize=8, color=sns.color_palette()[5], linewidth=4, label='Papernot')
plt.plot(x_axis, fid_CloudLeak, marker='X',markersize=8, color=sns.color_palette()[4], linewidth=4, label='Yu')
plt.plot(x_axis, fid_PriorMS, marker='s',markersize=8, color=sns.color_palette()[3], linewidth=4, label='Ours')



plt.legend(loc=4, fontsize=16) # 显示图例

plt.ylim((0, 1))
plt.xlabel('Perturbation-$\epsilon$',fontsize=20)
plt.ylabel('Transferability of AE',fontsize=20)
plt.xticks(x_axis, values)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)




plt.savefig(save_name+'.pdf', dpi=200, bbox_inches='tight',pad_inches=0.1)
plt.show()
sys.exit()
