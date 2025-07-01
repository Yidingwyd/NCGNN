# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 19:03:19 2025

@author: YidingWang
"""

from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import pandas as pd
import json, math

import os


original_value = os.environ.get("KMP_DUPLICATE_LIB_OK", None)


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"



def get_sites(structure):
    analyzer = SpacegroupAnalyzer(structure)
    conventional_struct = analyzer.get_conventional_standard_structure()
    sites = conventional_struct.sites
    comp_dict = {}
    for s in sites:
        comp_dict[str(s.frac_coords.tolist())] = s.species.formula
    return comp_dict

df = pd.read_csv('./dataset.csv')

dataset_dict = {}

for i in df.index:
    data_dict = {}
    cif_path = df.loc[i, 'cif']
    structure = Structure.from_file(cif_path)
    lattice = structure.lattice
    data_dict['a'] = lattice.a
    data_dict['b'] = lattice.b
    data_dict['c'] = lattice.c
    data_dict['alpha'] = lattice.alpha
    data_dict['beta'] = lattice.beta
    data_dict['gamma'] = lattice.gamma
    data_dict['comp'] = get_sites(structure)
    if len(data_dict['comp']) > 100:
        continue
    data_dict['target'] = float(df.loc[i, 'target'])
    dataset_dict[i] = data_dict


with open('./data.json', 'w', encoding='utf-8') as json_file:
    json.dump(dataset_dict, json_file, ensure_ascii=True, indent=4)



if original_value is not None:
    os.environ["KMP_DUPLICATE_LIB_OK"] = original_value  
else:
    del os.environ["KMP_DUPLICATE_LIB_OK"]  




