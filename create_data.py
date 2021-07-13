import numpy
numpy.random.seed(0)
import sys

mc_feature = {}
input0 = open("graph/BlogCatalog/BlogCatalog_motif.count")
id = 0
for line in input0:
    nums = line.split()
    feature = [int(x) for x in nums]
    if sum(feature)!=0:
        feature = [str(1.0 * x/(sum(feature))) for x in feature]   
    else:
        feature = [str(x) for x in feature]
    mc_feature[id] = feature
    id += 1
input0.close()

nodes, edges, node2vec_features, labels = [], [], {}, {}
input_label = open("graph/BlogCatalog/BlogCatalog.labels")
for line in input_label:
    nums = line.split()
    labels[nums[0]] = int(nums[1])
input_label.close()
    
input1 = open("emb/BlogCatalog.emb")
next(input1)
for line in input1:
    nums = line.split()
    if nums[0][:5]!="motif":
        node2vec_features[nums[0]] = nums[1:] + mc_feature[int(nums[0])]
        nodes.append(nums[0])
input1.close()

numpy.random.shuffle(nodes)
size = len(nodes)
print(size)
output_train1=open("BlogCatalog.feature_train", "w")
for i in range(0, int(7 * size / 10), 1):
    node = nodes[i]
    feature = node2vec_features[node]
    output_train1.write(str(labels[node]))
    for j in range(len(feature)):
        output_train1.write(" " + str(j) + ":" + feature[j])
    output_train1.write("\n")
output_train1.close()

output_val1=open("BlogCatalog.feature_val", "w")
for i in range(int(7 * size / 10), int(8 * size / 10), 1):
    node = nodes[i]
    feature = node2vec_features[node]
    output_val1.write(str(labels[node]))
    for j in range(len(feature)):
        output_val1.write(" " + str(j) + ":" + feature[j])
    output_val1.write("\n")
output_val1.close()

output_test1=open("BlogCatalog.feature_test","w")
for i in range(int(8 * size/10), size, 1):
    node = nodes[i]
    feature = node2vec_features[node]
    output_test1.write(str(labels[node]))
    for j in range(len(feature)):
        output_test1.write(" " + str(j) + ":" + feature[j])
    output_test1.write("\n")
output_test1.close()
