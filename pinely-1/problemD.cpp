#include <iostream>
using namespace std;

int main()
{
    int n, k;
    int mod = 1000000007;
    cin >> n >> k;

    auto prev = new int *[k + 2];
    for (int i = 0; i < k + 2; ++i)
    {
        prev[i] = new int[2];
        prev[i][0] = 0;
        prev[i][1] = 0;
    }
    auto cur = new int *[k + 2];
    for (int i = 0; i < k + 2; ++i)
    {
        cur[i] = new int[2];
        cur[i][0] = 0;
        cur[i][1] = 0;
    }
    prev[0][0] = 3;
    prev[1][1] = 1;
    for (int i = 1; i < n; ++i)
    {
        for (int j = 0; j < k + 1; ++j)
        {
            cur[j][0] += (prev[j][0] + prev[j][1]) % mod;
            cur[j][0] %= mod;
            cur[j][0] += (2 * prev[j][0]) % mod;
            cur[j][0] %= mod;
            if (j > 0)
            {
                cur[j][1] += (2 * prev[j - 1][1]) % mod;
                cur[j][1] %= mod;
                cur[j][1] += (prev[j - 1][0] + prev[j - 1][1]) % mod;
                cur[j][1] %= mod;
            }
        }
        for (int j = 0; j < k + 2; ++j)
        {
            prev[j][0] = cur[j][0];
            prev[j][1] = cur[j][1];
            cur[j][0] = 0;
            cur[j][1] = 0;
        }
    }
    cout << (prev[k][0] + prev[k][1]) % mod << endl;

    for (int i = 0; i < k + 2; ++i)
    {
        delete[] prev[i];
        delete[] cur[i];
    }
    delete[] prev;
    delete[] cur;
}