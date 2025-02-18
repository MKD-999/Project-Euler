#include <stdio.h>

int main()
{
    int sqrs = 0;
    int sum = 0;

    for (int i = 1; i <= 100; i++)
    {
        sqrs += (i * i);
        sum += i;
    }
      
    printf("%d\n", (sum * sum) - sqrs);

    return 0;
}