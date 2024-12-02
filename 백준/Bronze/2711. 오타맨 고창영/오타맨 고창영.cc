#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N;
    cin >> N;

    for(int i=0; i<N; i++)
    {
        int idx;
        string message;

        cin >> idx >> message;
        message.erase(idx-1, 1);
        cout << message <<endl;
    }
}