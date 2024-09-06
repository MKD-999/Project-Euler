#include <stdio.h>
#include <math.h>
#include <stdbool.h>

bool prime(int n)
{   
    int root = sqrt(n);
    for(int i = 2; i <= root; i++)
    {
        if(n % i == 0)
        {
            return false;
        }
    }

    return true;
}

int main()
{
    int cnt = 0;
    int i = 1;
    int ans = 0;
    
    while(cnt < 10002)
    {
        if(prime(i))
        {
            cnt += 1;
            ans = i;
            
        }

        i++;
    }

    printf("%d\n", ans);
    return 0;


}
