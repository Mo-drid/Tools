import os

for dirname, _, filenames in os.walk('E:/final data set/Data/test/images'):
    with open('test.txt', 'w') as f:
        for filename in filenames:
            print(os.path.join(dirname, filename[:-4]+'.jpg'))
            f.writelines('data/obj/'+ filename[:-4]+'.jpg'+'\n')
