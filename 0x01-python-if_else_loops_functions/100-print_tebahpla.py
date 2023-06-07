#!/usr/bin/python3
for x in reversed(range(97, 123)):
    if x % 2 == 0:
        print("{:c}".format(x), end="")
    else:
        print("{:c}".format(x - 32), end="")
