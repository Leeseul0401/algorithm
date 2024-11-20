#include <iostream>
#include <list>
#include <cmath>
#include <algorithm>

using namespace std;

int main() 
{
    while(true)
    {
        string str;
        string reverse_str;
        cin >> str;
        reverse_str = str;
        reverse(reverse_str.begin(), reverse_str.end());

        if(str == "0")
        {
            break;
        }
        int num;
        num = ceil(str.length() / 2);

        string result = "yes";
        for(int i=0; i<num; i++)
        {
            int temp = i + 1;
            // cout << "str[i] : " << str[i] << " str[-temp] : " << reverse_str[i] << endl;
            if(str[i] == reverse_str[i])
            {
                result = "yes";
            }
            else
            {
                result = "no";
                break;
            }
            
        }
        cout << result << endl;
    }
}