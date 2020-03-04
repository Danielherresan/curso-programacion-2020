import random

def roll():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    return (d1, d2)

# for i in range(0,2): print(roll().__getitem__(i))

