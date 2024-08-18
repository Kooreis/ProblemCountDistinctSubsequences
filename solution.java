Here is a Java console application that solves the problem:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a string:");
        String input = scanner.nextLine();
        System.out.println("Number of distinct subsequences: " + countSubsequences(input));
    }

    static int countSubsequences(String str) {
        int n = str.length();
        int[] last = new int[256];
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 0; i < 256; i++) {
            last[i] = -1;
        }
        for (int i = 1; i <= n; i++) {
            dp[i] = 2 * dp[i - 1];
            if (last[(int) str.charAt(i - 1)] != -1) {
                dp[i] = dp[i] - dp[last[(int) str.charAt(i - 1)]];
            }
            last[(int) str.charAt(i - 1)] = i - 1;
        }
        return dp[n];
    }
}
```

This program reads a string from the console, then calculates and prints the number of distinct subsequences in the string. The `countSubsequences` method uses dynamic programming to count the number of distinct subsequences. It maintains an array `dp` where `dp[i]` is the number of distinct subsequences of the first `i` characters in the string. It also maintains an array `last` where `last[j]` is the index of the last occurrence of character `j` in the string. For each character in the string, it doubles the number of distinct subsequences, then subtracts the number of distinct subsequences before the last occurrence of the current character.