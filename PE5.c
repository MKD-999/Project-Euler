#include <stdio.h>
#include <stdbool.h>


int main()
{
    int i = 2520;
    int j;
   
    while (true){
        
        bool chk = true;
        for (j = 2; j <= 20; j++)
        {
            if (i % j != 0)
            {
                i += 10;
                chk = false;
                break;
            }
            
        }
        
        if (chk == true)
        {
            printf("%d\n", i);
            break;
        }
        
    }

    return 0;
        
}
