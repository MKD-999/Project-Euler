#include <stdio.h>
#include <stdbool.h>

int main()
{   
    bool chk = false;
    int ans = 0;
    int vals[3];
    
    for (int m = 2; m < 1000; m++)
    {
        for (int n = 1; n < m; n++)
        {
            int a = (m * m) - (n * n);
            int b = 2 * m * n;
            int c = (m * m) + (n * n);
            
            if ((a + b + c) == 1000)
            {   
                
                chk = true;
                ans = a * b * c;
                vals[0] = a;
                vals[1] = b;
                vals[2] = c;

                break;
            }

        }

        if (chk == true)
        {
            printf("%d\n", ans);
            for (int i = 0; i <= 2; i++)
            {   
                printf("%d\n", vals[i]);
            }
            break;
        }
    }

    return 0;
}