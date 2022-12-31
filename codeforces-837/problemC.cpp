#include <bits/stdc++.h>
using namespace std;

int notprime[34050], arr[100500], mem[34050];
vector<int> primes;

void fastIO()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
}

void solve(int t)
{
    int n, k;
    cin >> n;
    map<int, int> mp;
    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }
    for (int i = 0; i < n; ++i)
    {
        k = arr[i];
        for (auto &prime : primes)
        {
            if (!(arr[i] % prime))
            {
                if (mem[prime] == t + 1)
                {
                    cout << "YES\n";
                    return;
                }
                mem[prime] = t + 1;
                while (!(k % prime))
                {
                    k /= prime;
                }
            }
        }
        if (k - 1 && mp[k])
        {
            cout << "YES\n";
            return;
        }
        mp[k]++;
    }
    cout << "NO\n";
}

int main()
{
    fastIO();

    for (int i = 2; i < 33333; ++i)
    {
        if (!notprime[i])
        {
            primes.push_back(i);
            for (int j = i; j < 33333; j += i)
            {
                notprime[j] = 1;
            }
        }
    }

    int t;
    cin >> t;
    while (t--)
    {
        solve(t);
    }
    return 0;
}