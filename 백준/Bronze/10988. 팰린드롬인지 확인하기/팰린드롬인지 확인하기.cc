#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string str;
    cin >> str;

    string temp;
    temp = str;
    reverse(str.begin(), str.end());
    if(str == temp) 
    {
        cout << 1 << endl;
    }
    else
    {
        cout << 0 << endl;
    }
}