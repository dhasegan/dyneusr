import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt

from dyneusr import DyNeuGraph
from dyneusr.datasets import make_trefoil
from dyneusr.tools import visualize_mapper_stages
from kmapper import KeplerMapper

# Generate synthetic dataset
dataset = make_trefoil(size=100)
X = dataset.data
y = dataset.target

# Define projections to compare
projections = ([0], [0,1], [1,2], [0, 2])

# Compare different sets of columns as lenses
for projection in projections:

	# Generate shape graph using KeplerMapper
	mapper = KeplerMapper(verbose=1)
	lens = mapper.fit_transform(X, projection=projection)
	graph = mapper.map(lens, X, nr_cubes=4, overlap_perc=0.3)

	# Visualize the stages of Mapper
	_ = visualize_mapper_stages(
		dataset, lens=lens, 
		graph=graph, cover=mapper.cover, 
		node_size=300, edge_size=0.5, edge_color='gray',
		layout="kamada_kawai", figsize=(20, 4),
		)

# Show 
plt.show()
