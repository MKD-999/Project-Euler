#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>


int* primesbelow(int n, int* primecount)
{
    bool* prime = (bool*) malloc((n + 1) * sizeof(bool)); // get array of nums below n + 1
    prime[0] = prime[1] = false;

    for(int i = 2; i <= n; i++)
    {   
        if( i != 2 && i % 2 == 0)
        {
            prime[i] = false;   // No even except 2 is prime
        }
        else
        {
            prime[i] = true;
        }
    }

    int sq = sqrt(n);
    
    for(int i = 3; i <= sq; i += 2) // Only odd nums are prime and max value is sqrt
    {
        if (prime[i] == true)
        {
            for(int j = i * i; j < n; j += (2 * i)) // Start from square and mark all multiples as not prime
            {
                prime[j] = false;
            }
        }
    }

    *primecount = 0; // to get number of primes
    for(int i = 2; i <= n; i++)
    {
        if (prime[i] == true)
        {
            (*primecount) ++;
        }
    }

    int* primearray = (int*) malloc( (*primecount) * sizeof(int)); // create array to which primes will be added
    int index = 0;

    for(int i = 2; i <= n; i++)
    {
        if(prime[i] == true)
        {
            primearray[index] = i;
            index++;
        }
    }

    free(prime);

    return primearray;

}

int main()
{   
    int limit = 2000000;
    int ptr;
    int* primes = primesbelow(limit, &ptr);
    long long ans = 0;

    for (int i = 0; i < ptr; i++)
    {
        ans += primes[i];
    }

    free(primes);
    printf("%lld\n", ans);
    
    return 0;


}