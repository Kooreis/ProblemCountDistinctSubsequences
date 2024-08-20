for i in range(1, n+1):
        count[i] = 2*count[i-1]
        if last[ord(s[i-1])] != -1:
            count[i] = count[i] - count[last[ord(s[i-1])]]
        last[ord(s[i-1])] = i-1