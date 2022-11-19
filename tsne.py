import csv
import numpy as np
from sklearn.manifold import TSNE
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import pandas as pd
from os.path import exists
from sklearn.decomposition import PCA


class DimRed:
    def __init__(self, dataset_name, exclude_list, n_bins, pca=True):
        self.csv_file = "features/" + dataset_name + "_all_features_normalized.csv"
        self.name_cat = pd.read_csv(self.csv_file, usecols=[0, 1])
        self.exclude_list = exclude_list
        self.n_bins = n_bins
        self.n_features = 5 + 5 * self.n_bins
        self.features = pd.read_csv(self.csv_file, usecols=np.arange(0,self.n_features+2))
        if pca:
            self.features = self.pca_red()
        if not exists("X_embedded.csv"):
            self.X_embedded = self.embed()
        else:
            self.X_embedded = pd.read_csv("X_embedded.csv")



    def embed(self):
        # perplexity = [30,40]
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore")
            tsne = TSNE(n_components=2, perplexity=40, random_state=42, n_jobs=-1)
            self.X = self.features.loc[:, ~self.features.columns.isin(['mesh name', 'category'])].to_numpy()
            X_embedded = tsne.fit_transform(self.X)
            name_cat_embed = pd.concat([self.name_cat, pd.DataFrame(X_embedded)], axis=1)
            name_cat_embed.to_csv("X_embedded.csv", index=False)
            return name_cat_embed


    def pca_red(self):
        self.X = self.features.loc[:, ~self.features.columns.isin(['mesh name', 'category'])].to_numpy()
        pca = PCA(n_components=50, random_state=42)
        self.X_pca = pca.fit_transform(self.X)
        name_cat_pca = pd.concat([self.name_cat, pd.DataFrame(self.X_pca)], axis=1)
        return name_cat_pca


    def plot(self):
        splt = sns.scatterplot(self.X_embedded, x="0", y="1", palette = sns.color_palette("hls", 17), style="category", hue="category", legend=True, s=150)
        sns.move_legend(splt, "upper center", ncol=9, bbox_to_anchor=(0.5,0), fontsize=16)
        plt.show()
