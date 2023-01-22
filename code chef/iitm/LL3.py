result = list()

for _ in range(int(input())):
    result.extend([int(x) for x in input().split()][1:])
result.sort()

for value in result:
    print(value, end=" ")
print()