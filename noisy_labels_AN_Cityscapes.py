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
annotations = a['annotations']
images = a['images']
for i in range(len(a['annotations'])):
    if np.random.random() < r:
        if a['annotations'][i]['category_id'] == 1:
            a['annotations'][i]['category_id'] = 6
        elif a['annotations'][i]['category_id'] == 6:
            a['annotations'][i]['category_id'] = 1
        elif a['annotations'][i]['category_id'] == 5:
            a['annotations'][i]['category_id'] = 7
        elif a['annotations'][i]['category_id'] == 7:
            a['annotations'][i]['category_id'] = 5
        elif a['annotations'][i]['category_id'] == 3:
            a['annotations'][i]['category_id'] = 4
        elif a['annotations'][i]['category_id'] == 4:
            a['annotations'][i]['category_id'] = 3
        count += 1
with open(p_g, 'w') as file:
    json.dump(a, file)

print(count)
