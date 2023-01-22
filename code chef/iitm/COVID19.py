
for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    new_list = []
    count = 1
    for i in range(n-1):
        if x[i+1]-x[i] <= 2:
            count += 1
        else:
            new_list.append(count)
            count = 1
    new_list.append(count)
    print(min(new_list), max(new_list))