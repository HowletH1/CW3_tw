from utils import *

data = load()
executed = select(data)
last = sorted_operations(executed)
for item in last_operations(last):
    print(item)
