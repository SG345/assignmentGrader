#include <iostream>
#include <string>
#include <unordered_set>
#include <algorithm>
#include <map>
#include <vector>
#include <iterator>
using namespace std;
 int findTrailingZeros( int  n)
{
     int count = 0;
 
   
    for ( int i=5; n/i>=1; i *= 5)
          count += n/i;
 
    return count;
}

int main()
{
	int n;
	cin>>n;

	int counter = 0;

	vector<int> F;
	for(int i = 0; i <= 100000; i++){
		if(findTrailingZeroes(i)==n){
			counter++;
			F.push_back(i);
		}
		if(findTrailingZeroes(i)>n)
			break;


	}
	cout<<F.size()<<endl;
	for(int i = 0; i < F.size(); i++){
		cout<<F[i]<<" ";
	}
	cout<<endl;
	return 0;
}
}