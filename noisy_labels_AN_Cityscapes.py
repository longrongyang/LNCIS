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
        # person -> rider
        if a['annotations'][i]['category_id'] == 24:
            a['annotations'][i]['category_id'] = 25
        # rider -> person
        elif a['annotations'][i]['category_id'] == 25:
            a['annotations'][i]['category_id'] = 24
        # truck -> bus
        elif a['annotations'][i]['category_id'] == 27:
            a['annotations'][i]['category_id'] = 28
        # bus -> truck
        elif a['annotations'][i]['category_id'] == 28:
            a['annotations'][i]['category_id'] = 27
        # motorcycle -> bicycle
        elif a['annotations'][i]['category_id'] == 32:
            a['annotations'][i]['category_id'] = 33
        # bicycle -> motorcycle
        elif a['annotations'][i]['category_id'] == 33:
            a['annotations'][i]['category_id'] = 32
        count += 1
with open(p_g, 'w') as file:
    json.dump(a, file)

print(count)
