#include <stdio.h>

int main()
{
    int arr[] = {10, 20, 30};
    int *ptr = arr + 2;
    printf("%d %d\n", *ptr, *(arr + 2));

    return 0;
}