#include <iostream>

using namespace std;

int main()
{
    string N;
    cin >> N;

    if(N == "M")
    {
        cout << "MatKor" << endl;
    } 
    else if(N == "W")
    {
        cout << "WiCys" << endl;
    }
    else if(N == "C")
    {
        cout << "CyKor" << endl;
    }
    else if(N == "A")
    {
        cout << "AlKor" << endl;
    }
    else if(N == "$")
    {
        cout << "$clear" << endl;
    }
}