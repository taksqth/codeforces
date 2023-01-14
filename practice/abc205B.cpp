#include <bits/stdc++.h>

using namespace std;

int i, n, a, ci[1005];

int main()
{
    scanf("%d", &n);
    for (i = 0; i < n; ++i)
    {
        scanf("%d", &a);
        ++ci[a];
    }
    for (i = 1; i <= n; ++i)
    {
        if (ci[i] != 1)
        {
            printf("No\n");
            return 0;
        }
    }
    printf("Yes\n");

    return 0;
}