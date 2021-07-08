python create_motif_count.py BlogCatalog
python reconstruct.py

python src/main.py --input graph/BlogCatalog/BlogCatalog.edges --input1 graph/BlogCatalog/reconstruct_network_new --output emb/BlogCatalog.emb --index 0.3 --weighted

#val 
python create_data.py
python LightGBM.py