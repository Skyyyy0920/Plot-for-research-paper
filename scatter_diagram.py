from sklearn.manifold import TSNE
from sklearn.datasets import load_iris, load_digits
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns

h, label = {}, {}
# path = 'h_trajectory'
# path = 'concat_embedding'
# path = 'concat_embedding_trajectory'
path = 'period_h'
# path = 'period_h_trajectory'
colors = ['#6c7197', '#d92405', '#3563eb', '#710162', '#fbbf45', '#03c383']
for user in range(10):
    h[user] = np.load(rf'./{path}/{user}_h2.npy')
    label[user] = np.load(rf'./{path}/{user}_category.npy')
    print(len(h[user]), len(label[user]))


for user in range(10):
    if user != 5:
        continue
    X_tsne = TSNE(n_components=2, random_state=33).fit_transform(h[user])
    color_label = []
    for i in range(len(label[user])):
        color_label.append(colors[label[user][i] - 1])
    plt.figure(figsize=(6, 6))

    for category in range(6):
        cluster_indices = np.where(label[user] == (category + 1))
        plt.scatter(X_tsne[cluster_indices, 0], X_tsne[cluster_indices, 1], c=colors[category],
                    label=rf"{4 * category}:00 - {4 * (category + 1)}:00")

    plt.xticks([])
    plt.yticks([])

    lg = plt.legend(loc='upper right')
    lg.set_title(title="time period", prop={'family': 'Times New Roman', 'size': 12})

    # plt.show()
    plt.savefig(rf'./{path}/user_{user}.pdf')
