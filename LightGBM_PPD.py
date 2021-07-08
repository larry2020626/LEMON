import xgboost as xgb
import numpy as np
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.metrics import f1_score
import lightgbm as lgb

path_train = sys.argv[1] + '_train'
path_test = sys.argv[1] + '_test'
path_val = sys.argv[1] + '_val'

dtrain = lgb.Dataset(path_train)
dtest = lgb.Dataset(path_test)
dval = lgb.Dataset(path_val)
test_l = open(path_test)
labels = []

input_file = open("graph/BlogCatalog/BlogCatalog.labels")
label_num = 0
for line in input:
    nums = line.split()
    t_label_num = int(nums[1])
    label_num = max(label_num, t_label_num)
input_file.close()
print(label_num)

#load label for test
for line in test_l.readlines():
    nums=line.split()
    labels.append(float(nums[0]))

param = {'learning_rate':0.1, 'num_leaves':7,'objective':'multiclass','num_class':label_num,'metric':'multi_error', 'lambda_l1':0.1, 'lambda_l2':0.1,'max_depth':9}
bst = lgb.train(param, dtrain, 1000, valid_sets = dval, early_stopping_rounds = 30)
print(path_test)
preds = bst.predict(path_test)
print(preds)
y_preds = []

for i in range(len(preds)):
    pre = list(preds[i]).index(max(preds[i]))
    y_preds.append(pre)

macro_f1 = f1_score(labels, y_preds, average='macro')
micro_f1 = f1_score(labels, y_preds, average='micro')

output = open("logging.file", "a")
print("macro_f1, micro_f1 : " + str(macro_f1) + " " + str(micro_f1) + "\n")
output.write(str(macro_f1) + " " + str(micro_f1) + "\n")
output.close()


"""
acc, err = 0,0
for i in range(len(preds)):
    pre = list(preds[i]).index(max(preds[i]))
    print(int(pre),int(labels[i]))
    if int(pre) == int(labels[i]):
        acc += 1
    else:
        err += 1
print(acc, err)
#loss = metrics.mean_squared_error(labels,preds)
#print(loss)
Acc = 1.0 * acc / (acc + err)
print("Accuracy is: " + str(Acc))
output = open("logging.file", "a")
output.write(str(Acc) + "\n")

output.close()
"""
