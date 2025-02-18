#include <stdio.h>

int main()
{   int first = 1;
    int second = 1;
    int ans = 0;
    int third = 0;


    while(third < 4000000)
        {   third = first + second;
            first = third - first;
            second = third;


            if (third % 2 == 0)
                {   ans += third;
            }

        }

    printf("%d\n",ans);

    return 0;


}
