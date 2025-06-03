# Imports
from IPython.display import Image
from pgmpy.utils import get_example_model

# Load the model
asia_model = get_example_model('asia')

# Visualize the network
# viz = asia_model.to_graphviz()
#viz.draw('asia.png', prog='neato')
#Image('asia.png')

import pprint

# Access attributes of the model
nodes = asia_model.nodes()
edges = asia_model.edges()
cpds = asia_model.get_cpds()

print(f"Nodes in the model: {nodes} \n")
print(f"Edges in the model: {edges} \n")
print(f"CPDs in the model: ")
pprint.pp(cpds)