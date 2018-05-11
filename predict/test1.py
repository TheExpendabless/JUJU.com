import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

dt=pd.read_csv("E:\python\project\predict\info2.csv",encoding="ansi")
data=dt.ix[:,[8,9,10,11,21,22,23,24,25]]
#3np.isnan(data).any()
#data.dropna(inplace=True)
#np.isnan(data).any()
label=dt[['totalprice']]
print(data.columns)

from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(data, label, random_state=0)
# 标准化
#sc = StandardScaler()
#X_train_std = sc.fit_transform(train_x)
#X_test_std = sc.transform(test_x)
# 主成分分析PCA
#pca = PCA()
#X_train_pca = pca.fit_transform(X_train_std)
#X_test_pca = pca.transform(X_test_std)


import xgboost as xgb
dtrain=xgb.DMatrix(train_x,label=train_y)
dtest=xgb.DMatrix(test_x)
params={'booster':'gblinear',
    'objective': 'reg:linear',

    'max_depth':4,
    'lambda':10,
    'subsample':0.75,
    'colsample_bytree':0.75,
    'min_child_weight':2,
    'eta': 0.025,
    'seed':0,
    'nthread':8,
     'silent':1}

watchlist = [(dtrain,'train')]
bst=xgb.train(params,dtrain,num_boost_round=10,evals=watchlist)
ypred=bst.predict(dtest)

# 设置阈值, 输出一些评价指标


from sklearn.metrics import mean_absolute_error
from sklearn.metrics import roc_auc_score
print ( mean_absolute_error(test_y,ypred))


bst.dump_model('dump3.raw.txt')


