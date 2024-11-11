#include <iostream>

int main()
{
    int N, M;
    std::cin >> N;

    for(int i=0; i<N; i++)
    {
        std::cin >> M;
        for(int j=0; j<M; j++)
        {
            printf("=");
        }
        printf("\n");
    }
}