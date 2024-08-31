#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool prime(int a)

{   int i;
    int root = sqrt(a);
    for(i = 2; i < root + 1; i++){
        if(a % i == 0){
            return false;
        }
    }

    return true;

}



int main()
{   int num = 13195;
    int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53};
    int i;
    int size = sizeof(primes)/sizeof(primes[0]);
    int tochk = 0;

    for(i = 0; i < size; i++ )
        {   if (num % primes[i] == 0)
            {
            }


        }
    printf("%d", tochk);
    return 0;

 }


