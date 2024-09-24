#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int triangle(int n)
{
    return (n * (n + 1)) / 2;
}

int main()
{   
    int i = 1;
    while (true)
    {
        int tri = triangle(i);
        int sq = sqrt(tri);

        int factors = 0;
        for(int j = 1; j <= sq; j ++)
        {
            if (tri % j == 0)
            {
                factors += 2;
            }
        }

        if (factors > 500)
        {   
            printf("%d\n", tri);
            break;
        }

        else
        {
            i++;
        }
        
    }

    return 0;
}