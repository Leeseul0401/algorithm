#define _CRT_SECURE_NO_WARNINGS
#include <time.h>
#include <iostream>
using namespace std;

int main()
{
    time_t current_time;
    struct tm* time_info;
    char time_str[80];

    current_time = time(NULL);
    time_info = localtime(&current_time);

    strftime(time_str, sizeof(time_str), "%Y-%m-%d", time_info);    
    printf(time_str);

    return 0;
}

