#include <iostream>
		using namespace std;
		int main()
		{
			int N;
			cin>>N;
			int hash[100005]={0};
			long long int ans=0;
			for(int i=0;i<N;i++)
			{
				int num;
				cin>>num;
				ans+=hash[num];
				hash[num]++;
			}
			cout<<ans<<endl;
			return 0;
		}
