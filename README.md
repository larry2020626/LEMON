# LEMON

This repository provides a reference implementation of LEMON algorithm.

## Requirements
python 2.7, gensim, networkx, numpy

### Input file
edgelist file, index of nodes are from 0 -> n-1
label file, 
node id, node label for one line.

### How to run
1. we adopt Orca <https://github.com/thocevar/orca> to compute motif count vector for each node.
```
orca.exe node 4 BlogCatalog.edges BlogCatalog_count.out
```
and get BlogCatalog_count.out


2. put motif into the network as super-vertex
```
python create_motif_count.py BlogCatalog
python reconstruct.py
```

3. to get embeddings for nodes and motifs
```
python src/main.py --input graph/BlogCatalog/BlogCatalog.edges --input1 graph/reconstruct_network_new --output emb/BlogCatalog.emb --index 0.3 --weighted
```
4.eval (params in LightGBM.py need to be set according to dataset)
```
python create_data.py
python LightGBM.py
```

This project referes the code of project node2vec: <https://github.com/aditya-grover/node2vec> .