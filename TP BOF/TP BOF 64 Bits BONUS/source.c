#include <stdio.h>

void vuln()
{
        printf("Good Luck! \n");
        char buf[500];
        gets(buf);
        printf("No root shell for you...\n");
}

int main()
{
    vuln();
}
