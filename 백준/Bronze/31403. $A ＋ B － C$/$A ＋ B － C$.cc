#include <iostream>
#include <string>

using namespace std;

int main()
{
    
    string N, M, temp;
    int P, result1, result2;

    cin >> N >> M >> P;
    temp = N + M;

    result2 = stoi(N) + stoi(M) - P;
    cout << result2 << endl;

    result1 = stoi(temp) - P;
    cout << result1 << endl;
}