"""
这是一种解决聚类问题的非监督式学习算法。这个方法简单地利用了一定数量的集群（假设K个集群）对给定数据进行分类。同一集群内的数据点是同类的，不同集群的数据点不同类。
还记得你是怎样从墨水渍中辨认形状的么？K均值算法的过程类似，你也要通过观察集群形状和分布来判断集群数量！

K均值算法如何划分集群：

从每个集群中选取K个数据点作为质心（centroids）。

将每一个数据点与距离自己最近的质心划分在同一集群，即生成K个新集群。

找出新集群的质心，这样就有了新的质心。

重复2和3，直到结果收敛，即不再有新的质心出现。

怎样确定K的值：

如果我们在每个集群中计算集群中所有点到质心的距离平方和，再将不同集群的距离平方和相加，我们就得到了这个集群方案的总平方和。

我们知道，随着集群数量的增加，总平方和会减少。但是如果用总平方和对K作图，你会发现在某个K值之前总平方和急速减少，但在这个K值之后减少的幅度大大降低，这个值就是最佳的集群数。
"""
#Import Library
from sklearn.cluster import KMeans

#Assumed you have, X (attributes) for training data set and x_test(attributes) of test_dataset
# Create KNeighbors classifier object model
k_means = KMeans(n_clusters=3, random_state=0)

# Train the model using the training sets and check score
k_means.fit(X)

#Predict Output
predicted= model.predict(x_test)