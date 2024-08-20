static int CountDistinctSubsequences(string str)
    {
        int n = str.Length;
        int[] last = new int[256];
        int[] dp = new int[n + 1];

        dp[0] = 1;
        for (int i = 0; i < 256; i++)
            last[i] = -1;