print("how much u want ROBUX")

robux = input("---> ")

import time

for percent in range(101):
    s = f"[{(percent // 10) * '■'}"
    s += f"{(10 - (percent // 10)) * '○'}] "
    s += f"{percent}"
    print(s, end="\r")
    time.sleep(0.1)

print("\ndone ^_^. now you have " + robux + " robux in yr balance")