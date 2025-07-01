import json, os
import pandas as pd
from sklearn.model_selection import KFold

# 读取JSON文件
file_path = './cpa_formation_energy_per_atom.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# 将数据转换为DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# 创建KFold对象
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# 保存训练集和测试集
for fold, (train_index, test_index) in enumerate(kf.split(df), 1):
    train_set = df.iloc[train_index].to_dict(orient='index')
    test_set = df.iloc[test_index].to_dict(orient='index')
    
    path = f'./{fold}'
    if not os.path.exists(path):
        os.makedirs(path)
    
    with open(path+'/train_set.json', 'w') as train_file:
        json.dump(train_set, train_file, indent=4)
        
    with open(path+'/val_set.json', 'w') as test_file:
        json.dump(test_set, test_file, indent=4)


