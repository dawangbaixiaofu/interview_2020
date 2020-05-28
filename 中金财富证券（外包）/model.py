from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('./total_woe.csv')
label = 'label'

# 特征筛选
# 根据IV贡献度，挑选出的特征是
features = ['age','education','education_num', 'martial_status','occupation','relationship','capital_gain']
features = [x+'_woe' for x in features]

train_index = np.random.choice(np.arange(len(df)), int(0.7*len(df)), replace=False)
test_index = list(set(np.arange(len(df)))-set(train_index))

train_x, train_y, test_x, test_y = df.loc[train_index, features], df.loc[train_index, label], df.loc[test_index, features], df.loc[test_index, label]

# 开始训练模型
logit = LogisticRegression()
logit.fit(train_x,train_y)
# 返回分类1的概率
logit_scores_proba = logit.predict_proba(train_x)
train_y_predict = logit.predict(train_x)
train_precision = precision_score(train_y,train_y_predict)
train_recall = recall_score(train_y,train_y_predict)
print('训练集准确率：',train_precision)
print('训练集召回率：',train_recall)

logit_scores = logit_scores_proba[:, 1]
# 画图
def plot_roc_curve(fpr, tpr, label=None):
    plt.figure(figsize=(12,10))
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0,1],[0,1], "k--") # 画直线做参考
    plt.axis([0,1,0,1])
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive rate")


# roc_curve根据分类结果和分类概率，返回false positive rate和true positive rate
fpr_logit, tpr_logit, thresh_logit = roc_curve(train_y, logit_scores)
# 画图
plot_roc_curve(fpr_logit,tpr_logit)
plt.show()
print('AUC Score : ', (roc_auc_score(train_y,logit_scores)))

# 验证测试集
logit_scores_proba_val = logit.predict_proba(test_x)
# 分类结果为1的概率
logit_scores_val = logit_scores_proba_val[:, 1]
test_y_predict = logit.predict(test_x)
# roc_curve根据分类结果和分类概率，返回false positive rage和true positive rate
fpr_logit_val, tpr_logit_val, thresh_logit_val = roc_curve(test_y, logit_scores_val)
ks_test = max(tpr_logit_val-fpr_logit_val)
print("the test group's ks is :", ks_test)

test_precision = precision_score(test_y, test_y_predict)
test_recall = recall_score(test_y, test_y_predict)
print('测试集准确率：', test_precision)
print('测试集召回率：', test_recall)


# 画图
plot_roc_curve(fpr_logit_val, tpr_logit_val)
plt.show()



print('AUC Score :', (roc_auc_score(test_y,logit_scores_val)))