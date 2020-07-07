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
    # vehicle
    super1 = np.array([2, 3, 4, 5, 6, 7, 8, 9])
    # outdoor
    super2 = np.array([10, 11, 13, 14, 15])
    # animal
    super3 = np.array([16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
    # accessory
    super4 = np.array([27, 28, 31, 32, 33])
    # sports
    super5 = np.array([34, 36, 36, 37, 38, 39, 40, 41, 42, 43])
    # kitchen
    super6 = np.array([44, 46, 47, 48, 49, 50, 51])
    # food
    super7 = np.array([52, 53, 54, 55, 56, 57, 58, 59, 60, 61])
    # furniture
    super8 = np.array([62, 63, 64, 65, 67, 70])
    # electronic
    super9 = np.array([72, 73, 74, 75, 76, 77])
    # appliance
    super10 = np.array([78, 79, 80, 81, 82])
    # indoor
    super11 = np.array([84, 85, 86, 87, 88, 89, 90])
    if np.random.random() < r:
        if 1 <= a['annotations'][i]['category_id'] <= 9:
            index = np.random.randint(0, 7)
            a['annotations'][i]['category_id'] = int(super1[index])
        elif 10 <= a['annotations'][i]['category_id'] <= 15:
            index = np.random.randint(0, 4)
            a['annotations'][i]['category_id'] = int(super2[index])
        elif 16 <= a['annotations'][i]['category_id'] <= 25:
            index = np.random.randint(0, 9)
            a['annotations'][i]['category_id'] = int(super3[index])
        elif 27 <= a['annotations'][i]['category_id'] <= 33:
            index = np.random.randint(0, 4)
            a['annotations'][i]['category_id'] = int(super4[index])
        elif 34 <= a['annotations'][i]['category_id'] <= 43:
            index = np.random.randint(0, 9)
            a['annotations'][i]['category_id'] = int(super5[index])
        elif 44 <= a['annotations'][i]['category_id'] <= 51:
            index = np.random.randint(0, 6)
            a['annotations'][i]['category_id'] = int(super6[index])
        elif 52 <= a['annotations'][i]['category_id'] <= 61:
            index = np.random.randint(0, 9)
            a['annotations'][i]['category_id'] = int(super7[index])
        elif 62 <= a['annotations'][i]['category_id'] <= 70:
            index = np.random.randint(0, 5)
            a['annotations'][i]['category_id'] = int(super8[index])
        elif 72 <= a['annotations'][i]['category_id'] <= 77:
            index = np.random.randint(0, 5)
            a['annotations'][i]['category_id'] = int(super9[index])
        elif 78 <= a['annotations'][i]['category_id'] <= 82:
            index = np.random.randint(0, 4)
            a['annotations'][i]['category_id'] = int(super10[index])
        elif 84 <= a['annotations'][i]['category_id'] <= 90:
            index = np.random.randint(0, 6)
            a['annotations'][i]['category_id'] = int(super11[index])
        count += 1
with open('', 'w') as file:
    json.dump(a, file)

print(count)
