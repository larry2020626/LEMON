import numpy as np
import networkx as nx
import random

class Graph():
	def __init__(self, nx_G, nx_G_new, index, is_directed, p, q):
		self.G = nx_G
		self.G1 = nx_G_new
		self.is_directed = is_directed
		self.p = p
		self.q = q
		self.index = index

	def LEMON_walk(self, walk_length, start_node):
		G = self.G
		G1 = self.G1
		alias_nodes = self.alias_nodes
		alias_edges = self.alias_edges

		walk = [start_node]
		#print("testing")
		#print(self.index)
		#print self.G.nodes(), self.G1.nodes()
		#exit(0)
		while len(walk) < walk_length:
			cur = walk[-1]
			x = random.random()
			if cur not in set(G1.nodes()):
				cur_nbrs = sorted(G.neighbors(cur))
			elif cur not in set(G.nodes()):
				cur_nbrs = sorted(G1.neighbors(cur))
			else:
				if x >= self.index:
					cur_nbrs = sorted(G.neighbors(cur))
				else:
					cur_nbrs = sorted(G1.neighbors(cur))

			if len(cur_nbrs) > 0:
				walk.append(random.choice(cur_nbrs))
			else:
				break

		return walk

	def simulate_walks(self, num_walks, walk_length):
		G = self.G
		walks = []
		nodes = list(G.nodes())
		print 'Walk iteration:'
		for walk_iter in range(num_walks):
			print str(walk_iter+1), '/', str(num_walks)
			random.shuffle(nodes)
			for node in nodes:
				walks.append(self.LEMON_walk(walk_length=walk_length, start_node=node))

		return walks

	def get_alias_edge(self, src, dst):
		G = self.G
		p = self.p
		q = self.q

		unnormalized_probs = []
		for dst_nbr in sorted(G.neighbors(dst)):
			if dst_nbr == src:
				unnormalized_probs.append(G[dst][dst_nbr]['weight']/p)
			elif G.has_edge(dst_nbr, src):
				unnormalized_probs.append(G[dst][dst_nbr]['weight'])
			else:
				unnormalized_probs.append(G[dst][dst_nbr]['weight']/q)
		norm_const = sum(unnormalized_probs)
		normalized_probs =  [float(u_prob)/norm_const for u_prob in unnormalized_probs]

		return alias_setup(normalized_probs)

	def preprocess_transition_probs(self):
		G = self.G
		is_directed = self.is_directed

		alias_nodes = {}
		for node in G.nodes():
			unnormalized_probs = [G[node][nbr]['weight'] for nbr in sorted(G.neighbors(node))]
			norm_const = sum(unnormalized_probs)
			normalized_probs =  [float(u_prob)/norm_const for u_prob in unnormalized_probs]
			alias_nodes[node] = alias_setup(normalized_probs)

		alias_edges = {}
		triads = {}

		if is_directed:
			for edge in G.edges():
				alias_edges[edge] = self.get_alias_edge(edge[0], edge[1])
		else:
			for edge in G.edges():
				alias_edges[edge] = self.get_alias_edge(edge[0], edge[1])
				alias_edges[(edge[1], edge[0])] = self.get_alias_edge(edge[1], edge[0])

		self.alias_nodes = alias_nodes
		self.alias_edges = alias_edges

		return


def alias_setup(probs):
	K = len(probs)
	q = np.zeros(K)
	J = np.zeros(K, dtype=np.int)

	smaller = []
	larger = []
	for kk, prob in enumerate(probs):
	    q[kk] = K*prob
	    if q[kk] < 1.0:
	        smaller.append(kk)
	    else:
	        larger.append(kk)

	while len(smaller) > 0 and len(larger) > 0:
	    small = smaller.pop()
	    large = larger.pop()

	    J[small] = large
	    q[large] = q[large] + q[small] - 1.0
	    if q[large] < 1.0:
	        smaller.append(large)
	    else:
	        larger.append(large)

	return J, q

def alias_draw(J, q):
	'''
	Draw sample from a non-uniform discrete distribution using alias sampling.
	'''
	K = len(J)

	kk = int(np.floor(np.random.rand()*K))
	if np.random.rand() < q[kk]:
	    return kk
	else:
	    return J[kk]
