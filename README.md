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

# Usage
## Define a customized dataset
As an example, one can refer to the [ICSD - CPA dataset](https://github.com/Yidingwyd/SSNGNN/blob/main/Kfold/cpa/cpa_formation_energy_per_atom.json), of which structures are from [ICSD](https://icsd.products.fiz-karlsruhe.de/) with formation energies calculated by Coherent Potential Approximation (CPA).  
The input of the SSNGNN should be saved as a python dictionary (named as `dataset dictionary`) in a `.json` file. 
* `dataset dictionary`:  
\- key - ID of each sample;  
\-  valule - `sample dictionary`.
* `sample dictionary`:  
\- keys `a`, `b`, `c`, `alpha`, `beta`, and `gamma` - the lattice parameters that describe the unit cell;  
\- key `comp` - `site dictionary`;  
\- key `target` - target (property) of the sample.  
* `site dictionary`:  
\- key - the relative positions of lattice sites, enclosed in square brackets [];  
\- value - the chemical compositions at those sites, which should be readable by pymatgen.  
A sample representing a BCC solid solution is shown below:  
![An example for a BCC sample](https://github.com/Yidingwyd/SSNGNN/blob/main/Kfold/cpa/fig1.png)  
If the solid solution exhibits a sublattice structure, where the composition varies across different lattice sites, the values in the `site dictionary` can also differ accordingly. A sample representing a perovskite solid solution is shown below:
![An example for a perovskite sample](https://github.com/Yidingwyd/SSNGNN/blob/main/Kfold/perovskite_band_gap/fig2.png)

 

