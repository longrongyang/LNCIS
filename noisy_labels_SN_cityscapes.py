import numpy as np
import json


def unjson(file):
    with open(file, 'r') as fo:
        dict = json.load(fo)
    return dict


# r is noise rate
r = 0.2

count = 0

p_a = ''
p_g = ''
a = unjson(p_a)
for i in range(len(a['annotations'])):
    if np.random.random() < r:
        id = np.array([24, 25, 26, 27, 28, 31, 32, 33])
        index = np.random.randint(0, 7)
        a['annotations'][i]['category_id'] = int(id[index])
        count += 1
with open(p_g, 'w') as file:
    json.dump(a, file)

print(count)
