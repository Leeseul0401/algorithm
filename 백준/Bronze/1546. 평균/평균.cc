#include <iostream>
// #include <stdio.h>

using namespace std;

int main()
{

    double N;
    double score[1000] = {};
    double result;
    double max;

    // scanf("%d", &N);
    cin >> N;
    cout.precision(8);
    for(int i=0; i<N; i++) 
    {
        cin >> score[i];
        if(score[i] > max) {
            max = score[i];
            
        }
        result += score[i];
        
    }
    
    cout << ( result / max * 100 ) / N;
}
