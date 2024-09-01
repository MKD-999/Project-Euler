#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool palindrome(int a)
{   
    char converted[10];
    sprintf(converted, "%d", a);

    if ( strlen(converted) % 2 == 0)
    {   
        int mid1 =  strlen(converted) / 2;
        
        char chk1[mid1];
        char chk2[mid1];
        
        // Numbers upto the first mid value
        for(int i = 0; i < mid1; i++) 
        {               
            chk1[i] = converted[i];
        }

        chk1[mid1] = '\0';
        

        // Numbers from the first mid value to the end of the string
        int ind = 0;
        for( int i = mid1; i < strlen(converted); i++) 
        {                                   
            chk2[ind++] = converted[i];
            
        }
        chk2[mid1] = '\0';

        
        // Reversing
        int total = strlen(chk2) - 1;
        char reversed[mid1];

        for(int i = 0; i <= total; i++)
        {
            reversed[i] = chk2[total - i];
        }
        reversed[mid1] = '\0';
        
        if (strcmp(chk1, reversed) == 0)
        {
            return true;
        }

        else
        {
            return false;
        }

    }

    else
    {   
        int mid = strlen(converted) / 2;
        // Get first numbers from 0 to mid

        char chk1[mid];
        char chk2[mid];

        for(int i = 0; i <= mid; i++)
        {
            chk1[i] = converted[i];
        }
        chk1[mid + 1] = '\0';
        

        // Get number from mid to end of string

        int ind = 0;
        
        for(int i = mid; i < strlen(converted); i++)
        {
            chk2[ind++] = converted[i];
        }

        chk2[mid + 1] = '\0';
        
        
        // Reversing the string

        int total = strlen(chk2) - 1;
        char reversed[mid];

        for(int i = 0; i <= total; i++)
        {
            reversed[i] = chk2[total - i];

        }
        reversed[mid + 1] = '\0';

        if (strcmp(chk1,reversed) == 0)
        {
            return true;
        }

        else
        {
            return false;
        }
    }
}

int main()
{
    int ans = 0;

    for( int i = 100; i < 1000; i++)
    {
        for (int j = i+1; j < 1000; j++)
        {
            if (palindrome(i * j) == true)
            {
                if ((i * j) > ans)
                {
                     ans = i * j;
                }
            }
        }
    }
    printf("%d\n", ans);
    return 0;
}