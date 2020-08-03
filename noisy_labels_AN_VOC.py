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
        if a['annotations'][i]['category_id'] == 3:
            a['annotations'][i]['category_id'] = 1
            count += 1
        elif a['annotations'][i]['category_id'] == 11:
            a['annotations'][i]['category_id'] = 9
            count += 1
        elif a['annotations'][i]['category_id'] == 6:
            a['annotations'][i]['category_id'] = 7
            count += 1
        elif a['annotations'][i]['category_id'] == 17:
            a['annotations'][i]['category_id'] = 13
            count += 1
        elif a['annotations'][i]['category_id'] == 2:
            a['annotations'][i]['category_id'] = 14
            count += 1
        elif a['annotations'][i]['category_id'] == 14:
            a['annotations'][i]['category_id'] = 2
            count += 1
        elif a['annotations'][i]['category_id'] == 8:
            a['annotations'][i]['category_id'] = 12
            count += 1
        elif a['annotations'][i]['category_id'] == 12:
            a['annotations'][i]['category_id'] = 8
            count += 1
with open(p_g, 'w') as file:
    json.dump(a, file)

print(count)
