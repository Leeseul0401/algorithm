#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main()
{
    int N;
    cin >> N;

    for(int i=0; i<N; i++)
    {
        string M;
        cin >> M;
        
        transform(M.begin(), M.end(), M.begin(), ::tolower);
        cout << M << endl;
    }

}