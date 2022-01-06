import os

path = r'C:\Users\EF-QA-11\AppData\Local'
f = os.walk(path)

print('*'*10)
for root, dirs, file_ in f:
    print(root, file_)
    # route = os.path.join(root, file_)
    # print(route, ":" , str(os.path.getsize(route)))
print('*'*10)