#!/usr/bin/python3
output = ""
for i in range(0, 100):
    output += "{:02d}".format(i)
    if i < 99:
        output += ", "
output += "\n"
print(output, end="")
