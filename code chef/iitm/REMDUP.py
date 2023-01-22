for _ in range(int(input())):
    __ = input()
    a = set(map(int, input().split()))
    print(*sorted(a), sep=' ')