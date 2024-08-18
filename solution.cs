Here is a C# console application that solves the problem:

```csharp
using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("Enter a string: ");
        string input = Console.ReadLine();
        Console.WriteLine("Number of distinct subsequences: " + CountDistinctSubsequences(input));
    }

    static int CountDistinctSubsequences(string str)
    {
        int n = str.Length;
        int[] last = new int[256];
        int[] dp = new int[n + 1];

        dp[0] = 1;
        for (int i = 0; i < 256; i++)
            last[i] = -1;

        for (int i = 1; i <= n; i++)
        {
            dp[i] = 2 * dp[i - 1];
            if (last[str[i - 1]] != -1)
                dp[i] = dp[i] - dp[last[str[i - 1]]];
            last[str[i - 1]] = (i - 1);
        }

        return dp[n];
    }
}
```

This program counts the number of distinct subsequences in a string. It uses dynamic programming to calculate the number of distinct subsequences for all prefixes of the string, and then returns the count for the entire string. The last occurrence of all possible characters is also stored in an array. If a character is seen again, its last occurrence is subtracted from the count.