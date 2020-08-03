import numpy as np
import json


def unjson(file):
    with open(file, 'r') as fo:
        dict = json.load(fo)
    return dict


# r is noise rate
r = 0.2

count = 0
c = 0

p = ''
a = unjson(p)
for i in range(len(a['annotations'])):
    if a['annotations'][i]['category_id'] == 3:
        if np.random.random() < r:
            a['annotations'][i]['category_id'] = 1
            count += 1
    elif a['annotations'][i]['category_id'] == 11:
        if np.random.random() < r:
            a['annotations'][i]['category_id'] = 9
            count += 1
    elif a['annotations'][i]['category_id'] == 6:
        if np.random.random() < r:
            a['annotations'][i]['category_id'] = 7
            count += 1
    elif a['annotations'][i]['category_id'] == 17:
        if np.random.random() < r:
            a['annotations'][i]['category_id'] = 13
            count += 1
    elif a['annotations'][i]['category_id'] == 2:
        if np.random.random() < r:
            a['annotations'][i]['category_id'] = 14
            count += 1
    elif a['annotations'][i]['category_id'] == 14:
        if np.random.random() < r:
            a['annotations'][i]['category_id'] = 2
            count += 1
    elif a['annotations'][i]['category_id'] == 8:
        if np.random.random() < r:
            a['annotations'][i]['category_id'] = 12
            count += 1
    elif a['annotations'][i]['category_id'] == 12:
        if np.random.random() < r:
            a['annotations'][i]['category_id'] = 8
            count += 1
    else:
        c = c + 1
with open('', 'w') as file:
    json.dump(a, file)

print(count)
