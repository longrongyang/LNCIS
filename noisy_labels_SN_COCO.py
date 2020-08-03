import numpy as np
import json


def unjson(file):
    with open(file, 'r') as fo:
        dict = json.load(fo)
    return dict

# r is noise rate
r = 0.2

count = 0

p = ''
a = unjson(p)
for i in range(len(a['annotations'])):
    if np.random.random() < r:
        id = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13,
                       14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                       24, 25, 27, 28, 31, 32, 33, 34, 35, 36, 37,
                       38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49,
                       50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                       61, 62, 63, 64, 65, 67, 70, 72, 73, 74, 75,
                       76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87,
                       88, 89, 90])
        index = np.random.randint(0, 79)
        a['annotations'][i]['category_id'] = int(id[index])
        count += 1
with open('', 'w') as file:
    json.dump(a, file)

print(count)
