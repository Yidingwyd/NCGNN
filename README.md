# SSNGNN
Solid Solution Nested Graph Neural Network (without edge features in the compositional graph)

**Note:** This package is the version without edge features in the compositional graph.  
          For the version with edge features in the compositional graph, e.g., study of the chemical short-range order (SRO) in solid solutions, please refer to the second version [SSNGNN_v2](https://github.com/Yidingwyd/SSNGNN_v2).  

# Brief review
SSNGNN provides a unified end-to-end representation learning framework for solid solution materials.   
In simple terms, SSNGNN consists of two layers of graph representations: an inner compositional graph and an outer structural graph.  
   * The inner compositional graph captures the compositional information of the solid solution by representing different elements at each lattice site.  
   * The outer structural graph models the overall crystal structure, aggregating features from the compositional graphs based on the spatial arrangement of lattice sites.  

# How to cite
Our paper is in submission now.

# Prerequisites
This Python package requires: pytorch, torch_scatter, scikit-learn, pymatgen, pandas, numpy, json.


