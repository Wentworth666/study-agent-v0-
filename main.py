import os
import sys


if len(sys.argv) < 2:
    print("Too few arguments")
elif not os.path.exists(sys.argv[1]):
    print("doesn't exist")
else:
    with open(sys.argv[1], "r") as file:
        content = file.readlines()
        print(content)
