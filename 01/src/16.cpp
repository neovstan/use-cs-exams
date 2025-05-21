#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve() {
  vector<int> dp(2e8 + 1);
  for (int i = 1; i <= 2e8; ++i)
    dp[i] = dp[i / 9] + i % 3;
  return count(next(dp.begin(), 1e8), dp.end(), 0);
}

int main() {
  auto answer = solve();
  cout << answer << endl;
}

// Answer: 6561