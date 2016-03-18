#include <stdio.h>

int main()
{
	int n = 12;

	char *pc;

	pc = (char*)&n; //cast int pointer to char pointer

	if(*pc != 0)
	   printf("Little Endian\n");
	else
	   printf("Big Endian\n");

	return 0;
}
