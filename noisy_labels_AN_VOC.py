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
        # bird -> aeroplane
        if a['annotations'][i]['category_id'] == 3:
            a['annotations'][i]['category_id'] = 1
        # diningtable -> chair
        elif a['annotations'][i]['category_id'] == 11:
            a['annotations'][i]['category_id'] = 9
        # bus -> car
        elif a['annotations'][i]['category_id'] == 6:
            a['annotations'][i]['category_id'] = 7
        # sheep -> horse
        elif a['annotations'][i]['category_id'] == 17:
            a['annotations'][i]['category_id'] = 13
        # bicycle -> motorbike
        elif a['annotations'][i]['category_id'] == 2:
            a['annotations'][i]['category_id'] = 14
        # motorbike -> bicycle
        elif a['annotations'][i]['category_id'] == 14:
            a['annotations'][i]['category_id'] = 2
        # cat -> dog
        elif a['annotations'][i]['category_id'] == 8:
            a['annotations'][i]['category_id'] = 12
        # dog -> cat
        elif a['annotations'][i]['category_id'] == 12:
            a['annotations'][i]['category_id'] = 8
        count += 1
with open(p_g, 'w') as file:
    json.dump(a, file)

print(count)
