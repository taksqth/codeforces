#include <bits/stdc++.h>

using namespace std;

int i, n, d, ret;

int main()
{
    scanf("%d", &n);
    ret = 0;
    for (i = 0; i < n; ++i)
    {
        scanf("%d", &d);
        ret += max(0, d - 10);
    }
    printf("%d\n", ret);

    return 0;
}