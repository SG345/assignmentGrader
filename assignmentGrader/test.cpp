#include <stdio.h>

void quickSort( int[], int, int);
int partition( int[], int, int);


//QUICKSORT
int main() 
{
	int n;
scanf("%d", &n);

int a[10002];
	int i;
	for(i = 0; i < n; ++i)
		scanf("%d", &a[i]);

	quickSort( a, 0, n);

	for(i = 0; i < n; ++i)
		printf("%d ", a[i]);

}



void quickSort( int a[], int l, int r)
{
   int j;

   if( l < r ) 
   {
   	// divide and conquer
        j = partition( a, l, r);
       quickSort( a, l, j-1);
       quickSort( a, j+1, r);
   }
	
}



int partition( int a[], int l, int r) {
   int pivot, i, j, t;
   pivot = a[l];
   i = l; j = r+1;
		
   while( 1)
   {
   	do ++i; while( a[i] <= pivot && i <= r );
   	do --j; while( a[j] > pivot );
   	if( i >= j ) break;
   	t = a[i]; a[i] = a[j]; a[j] = t;
   }
   t = a[l]; a[l] = a[j]; a[j] = t;
   return j;
}

