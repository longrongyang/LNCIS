import numpy as np
import json


def unjson(file):
    with open(file, 'r') as fo:
        dict = json.load(fo)
    return dict


# r is noise rate
r = 0.4

count = 0

a = unjson('')
for i in range(len(a['annotations'])):
    if np.random.random() < r:
        a['annotations'][i]['category_id'] = np.random.randint(1, 20)
        count += 1
with open('', 'w') as file:
    json.dump(a, file)

print(count)
