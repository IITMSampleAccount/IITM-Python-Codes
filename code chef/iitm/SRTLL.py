for _ in range(int(input())):
    __ = input()
    a = list(map(int, input().split()))
    print(*sorted(a), sep=' ')