import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

dataset = pd.read_csv('S1018bf.csv')
dataset = dataset.dropna()
# print(dataset.head())

# 提取特征和类别
X = dataset.loc[:, 'Spectral.Index':'variability_index']
y = dataset.loc[:, 'Optical.Class']

# 标准化
normalizer = preprocessing.StandardScaler()
scaled = normalizer.fit_transform(X.values)
X = pd.DataFrame(scaled)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


def fit(name, model):
    # 训练及预测
    model.fit(X_train, y_train)
    predict_data = model.predict(X_test)

    # 准确率
    accuracy = np.mean(predict_data == y_test)
    print('{:>4}  {:.4f}'.format(name, accuracy))

    return accuracy


# 建立模型。设置算法内核类型, 有 'linear’, ‘poly’, ‘rbf’, ‘sigmoid’. 惩罚参数为 1, 一般为 10 的幂次方
svc = SVC(kernel='rbf', C=1, gamma='scale')  # 0.8399
# svc = SVC(kernel='poly', degree=1, C=1, gamma='auto')  # 0.8333
# svc = SVC(kernel='linear', C=0.1)  # 0.8366
fit('SVC', svc)

# 建立 MLP 神经网络模型, MLP 的求解方法为 adam, 可选 lbfgs、sgd, 正则化惩罚 alpha = 0.1
mlp = MLPClassifier(solver='adam',
                    hidden_layer_sizes=(100, 50, 100, 50, 100),
                    learning_rate='constant',
                    learning_rate_init=0.01,
                    max_iter=500,
                    alpha=0.1)
fit('MLP', mlp)

# 建立 KNN 模型, 邻居数选为 7, 默认为 5
knn = KNeighborsClassifier(n_neighbors=7)  # 0.7908
fit('KNN', knn)

# 建立逻辑回归模型, 惩罚参数为 100
lr = LogisticRegression(C=100, max_iter=1000, solver='liblinear', class_weight='balanced')  # 0.83
fit('LR', lr)

# 建立决策树模型, 选择算法为熵增益, 可选 gini, entropy, 默认为 gini
dt = DecisionTreeClassifier(criterion='entropy', class_weight='balanced')  # ~0.81
fit('DT', dt)

bag = BaggingClassifier(base_estimator=dt, n_estimators=100)  # ~0.86
fit('BAG', bag)

rf = RandomForestClassifier(n_estimators=100, criterion='entropy', class_weight='balanced')  # ~0.86
fit('RF', rf)
