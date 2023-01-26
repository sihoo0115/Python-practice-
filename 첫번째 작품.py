import random
import time
from time import localtime
hour=time.localtime()[3]
num=random.randint(0,10)
a = "Life is too short, You need Python"
b = "I ate all %d apples at %d o'clock." % (num, hour)
print(b)
print(f"지금은 {hour}시 입니다.")
