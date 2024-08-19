def count_distinct_subsequences(s):
    n = len(s)
    count = [0 for _ in range(n+1)]
    last = [-1 for _ in range(256)]
    count[0] = 1