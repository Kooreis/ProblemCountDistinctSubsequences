Here is a Python console application that counts the number of distinct subsequences in a string:

```python
def count_distinct_subsequences(s):
    n = len(s)
    count = [0 for _ in range(n+1)]
    last = [-1 for _ in range(256)]
    count[0] = 1
    for i in range(1, n+1):
        count[i] = 2*count[i-1]
        if last[ord(s[i-1])] != -1:
            count[i] = count[i] - count[last[ord(s[i-1])]]
        last[ord(s[i-1])] = i-1
    return count[n]

def main():
    s = input("Enter a string: ")
    print("Number of distinct subsequences: ", count_distinct_subsequences(s))

if __name__ == "__main__":
    main()
```

This program works by first initializing an array `count` of size `n+1` where `n` is the length of the string. `count[i]` will store the count of distinct subsequences of length `i` in the string. It also initializes an array `last` of size 256 to store the last occurrence of all possible characters of the ASCII.

The program then iterates over the string, and for each character, it calculates two counts: 

1. `2*count[i-1]`: This considers the current character and counts all subsequences including the ones without the current character.
2. `count[last[ord(s[i-1])]]`: Since the current character is included, the count of subsequences with this character becomes the same as the count of subsequences without this character.

The final count of distinct subsequences is stored in `count[n]`.

The `main` function prompts the user to enter a string, and then it prints the number of distinct subsequences in the string.