class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.length(), n = t.length();
        if (m < n) return 0;

        // dp[j] stores the count of subsequences matching t[0...j-1]
        vector<unsigned long long> dp(n + 1, 0);
        dp[0] = 1; // An empty string t has 1 match (empty subsequence)

        for (int i = 1; i <= m; ++i) {
            // Iterate backwards to update in-place without overwriting previous state
            for (int j = n; j >= 1; --j) {
                if (s[i - 1] == t[j - 1]) {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return dp[n];
    }
};