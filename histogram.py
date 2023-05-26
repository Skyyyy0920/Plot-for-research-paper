import numpy as np
import pylab as pl
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sns

########################################################################################################################
# 全局设置
sns.set(style='whitegrid', color_codes=True)  # 设置绘图风格和颜色
plt.figure(figsize=(18, 6.5))
plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内

########################################################################################################################
# 子图设置
plt.subplot(131)

data = [[0.14115545, 0.30077427, 0.373436569, 0.44192972],
        [0.146515783, 0.337701013, 0.412745682, 0.509231686],
        [0.154258487, 0.346634902, 0.427039905, 0.502680167],
        [0.144133413, 0.337701013, 0.419297201, 0.500297796],
        [0.147706968, 0.338296605, 0.412745682, 0.499702204]]

plt.xlabel('K', fontdict={'family': 'Times New Roman', 'size': 35})
plt.yticks(fontproperties='Times New Roman', size=25)
plt.xticks(fontproperties='Times New Roman', size=25)

X = np.array([0.9, 0.9 * 2, 0.9 * 3, 0.9 * 4])  # X是1,2,3,4,5,6,7,8,柱的个数
plt.bar(X + 0.55, data[0], alpha=0.7, width=0.13, facecolor='#C43302', edgecolor='black', label='1-ary', lw=1)
plt.bar(X + 0.68, data[1], alpha=0.7, width=0.13, facecolor='#EDAA25', edgecolor='black', label='2-ary', lw=1)
plt.bar(X + 0.81, data[2], alpha=0.7, width=0.13, facecolor='#B7BF99', edgecolor='black', label='3-ary', lw=1)
plt.bar(X + 0.94, data[3], alpha=0.7, width=0.13, facecolor='#0A7373', edgecolor='black', label='4-ary', lw=1)
plt.bar(X + 1.07, data[4], alpha=0.7, width=0.13, facecolor='#010221', edgecolor='black', label='5-ary', lw=1)
pos = X + 0.9 - 0.08
plt.xticks(pos.tolist(), ['1', '5', '10', '20'])

plt.legend(ncol=1, loc="upper left", columnspacing=0.2,
           prop={'family': 'Times New Roman', 'size': 17})
plt.tick_params(axis='x', length=0)

#######################################
plt.subplot(132)

data = [[0.274799493, 0.487125369, 0.560785141, 0.632756437],
        [0.279020684, 0.503588012, 0.591177712, 0.66230477],
        [0.283875053, 0.508442381, 0.590333474, 0.663993246],
        [0.281553398, 0.506120726, 0.585056986, 0.654495568],
        [0.275854791, 0.505487547, 0.584634867, 0.662937949]]

plt.xlabel('K', fontdict={'family': 'Times New Roman', 'size': 35})
plt.yticks(fontproperties='Times New Roman', size=25)
plt.xticks(fontproperties='Times New Roman', size=25)

plt.bar(X + 0.55, data[0], alpha=0.7, width=0.13, facecolor='#C43302', edgecolor='black', label='1-ary', lw=1)
plt.bar(X + 0.68, data[1], alpha=0.7, width=0.13, facecolor='#EDAA25', edgecolor='black', label='2-ary', lw=1)
plt.bar(X + 0.81, data[2], alpha=0.7, width=0.13, facecolor='#B7BF99', edgecolor='black', label='3-ary', lw=1)
plt.bar(X + 0.94, data[3], alpha=0.7, width=0.13, facecolor='#0A7373', edgecolor='black', label='4-ary', lw=1)
plt.bar(X + 1.07, data[4], alpha=0.7, width=0.13, facecolor='#010221', edgecolor='black', label='5-ary', lw=1)
plt.xticks(pos.tolist(), ['1', '5', '10', '20'])

plt.legend(ncol=1, loc="upper left", columnspacing=0.2,
           prop={'family': 'Times New Roman', 'size': 17})
plt.tick_params(axis='x', length=0)

###################################
plt.subplot(133)

data = [[0.25388601, 0.501850481, 0.576609919, 0.621761658],
        [0.240562546, 0.52553664, 0.609178386, 0.676535899],
        [0.25684678, 0.532938564, 0.621021466, 0.688378979],
        [0.248704663, 0.521835677, 0.609918579, 0.675055514],
        [0.247964471, 0.515914138, 0.596595115, 0.671354552]]

plt.xlabel('K', fontdict={'family': 'Times New Roman', 'size': 35})
plt.yticks(fontproperties='Times New Roman', size=25)
plt.xticks(fontproperties='Times New Roman', size=25)

plt.bar(X + 0.55, data[0], alpha=0.7, width=0.13, facecolor='#C43302', edgecolor='black', label='1-ary', lw=1)
plt.bar(X + 0.68, data[1], alpha=0.7, width=0.13, facecolor='#EDAA25', edgecolor='black', label='2-ary', lw=1)
plt.bar(X + 0.81, data[2], alpha=0.7, width=0.13, facecolor='#B7BF99', edgecolor='black', label='3-ary', lw=1)
plt.bar(X + 0.94, data[3], alpha=0.7, width=0.13, facecolor='#0A7373', edgecolor='black', label='4-ary', lw=1)
plt.bar(X + 1.07, data[4], alpha=0.7, width=0.13, facecolor='#010221', edgecolor='black', label='5-ary', lw=1)
plt.xticks(pos.tolist(), ['1', '5', '10', '20'])

plt.legend(ncol=1, loc="upper left", columnspacing=0.2,
           prop={'family': 'Times New Roman', 'size': 17})  # label的位置在左上，没有这句会找不到label去哪了
plt.tick_params(axis='x', length=0)

plt.tight_layout()
# plt.show()

# ######################保存#############################
pdf = PdfPages('exp.pdf')
pdf.savefig()
plt.close()
pdf.close()
