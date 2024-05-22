class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[] for _ in range(n+1)]
        dp[-1] = [[]]  # base case
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i:j] == s[i:j][::-1]:  # if s[i:j] is palindrome
                    for each in dp[j]:
                        dp[i].append([s[i:j]] + each)
        return dp[0]
