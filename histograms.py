import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#print(df)

df = pd.read_csv('basic_mesh_info.csv')
# vertices = df['n_vertices']
# vertices = [x for x in vertices if x <= 20000]
# plt.hist(vertices, bins=80)
# plt.xlabel('num_vertices')
# plt.ylabel('frequency')
# plt.title("Distribution of number of vertices")

#category histogram
df2 = df['category'].value_counts().plot(kind ='barh')
plt.ylabel('category')
plt.xlabel('frequency')
plt.title("Distribution by category")

#faces histogram
# faces = df['n_faces']
# faces = [x for x in faces if x <= 20000]
# plt.hist(faces, bins=80)
# plt.xlabel('num_faces')
# plt.ylabel('frequency')
# plt.title("Distribution of number of faces")


plt.show()



#groups = df.groupby(['n_vertices', pd.cut(df.n_vertices, [0, 5000, 10000])])
#df2 = groups['n_vertices'].value_counts().plot(kind ='bar')

#df2.axes.set_xticks([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,1100, 1200, 1300, 1400])

#df3 = df['category'].value_counts().plot(kind ='bar')

#df4 = df['n_faces'].value_counts().plot(kind ='bar')

#groups = df.groupby(['n_vertices', pd.cut(df.n_vertices, [0, 5000, 10000])])

#df2 = df.groupby(['n_vertices']).mean()
#df2 = df.groupby(['category']).mean()
#df3 = df.loc[df['category']== 'animal']
#df2.head() 

#print(df2.index)
#plt.bar(df2.index, df2['n_vertices'].values)
#plt.bar(df2.index, df2['n_faces'].values)

#plt.hist(df3['n_vertices'])



