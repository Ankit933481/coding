class Solution {
public:
    int distinctSubseqII(string s) {
        int MOD = 1e9 + 7;
        vector<long long> ends_with(26, 0);
        long long total_sum = 0;

        for (char c : s) {
            int idx = c - 'a';
            // New distinct subsequences ending in character 'c'
            long long new_count = (1 + total_sum) % MOD;
            
            // Update total sum by adding new count and subtracting old count for character 'c'
            total_sum = (total_sum + new_count - ends_with[idx] + MOD) % MOD;
            ends_with[idx] = new_count;
        }

        return total_sum;
    }
};