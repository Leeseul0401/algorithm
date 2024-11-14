#include <iostream>
using namespace std;

int main()
{
    int N, M, K;
    cin >> N >> M >> K;

    int A;
    A = min(M, K);

    int B, C;
    B = N - M;
    C = N - K;

    int result;
    result = min(B, C);
    cout << A + result;
}