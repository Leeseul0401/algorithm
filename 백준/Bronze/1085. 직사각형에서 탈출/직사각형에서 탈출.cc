#include <iostream>
using namespace std;

int main()
{
    int x, y, w, h;
    
    cin >> x >> y >> w >> h;

    int resultX, resultY;

    resultX = abs(x - w);
    resultY = abs(y - h);

    if(resultX > x) 
    {
        resultX = x;
    }

    if(resultY > y)
    {
        resultY = y;
    }

    cout << min(resultX, resultY) << endl;
}