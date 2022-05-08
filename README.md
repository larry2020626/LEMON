# LEMON

This repository provides an implementation of LEMON in [1], a network embedding algorithm via structural pattern motifs,  which bridges connectivity and structural similarity in a uniform representation,  .

### Requirements
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



### Reference

[1] Shao P, Yang Y, Xu S, et al. Network Embedding via Motifs[J]. ACM Transactions on Knowledge Discovery from Data (TKDD), 2021, 16(3): 1-20.

```bib
@article{shao2021network,
  title={Network Embedding via Motifs},
  author={Shao, Ping and Yang, Yang and Xu, Shengyao and Wang, Chunping},
  journal={ACM Transactions on Knowledge Discovery from Data (TKDD)},
  volume={16},
  number={3},
  pages={1--20},
  year={2021},
  publisher={ACM New York, NY}
}
```