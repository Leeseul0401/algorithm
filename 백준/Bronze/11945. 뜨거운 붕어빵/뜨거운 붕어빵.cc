#include <iostream>
#include <list>

using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;
    
    int numbers[M];
    
    for(int i=0; i<N; i++) 
    {
        string number;
        cin >> number;
            
        for(int j=0; j<M; j++)
        {
            int a = number[j] - '0';
            numbers[j] = a;
        }

        for(int z=M-1; z>=0; z--)
        {
            cout << numbers[z];
        }
        cout<<endl;
        
        
    }
}