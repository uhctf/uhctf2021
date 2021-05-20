#include <iostream>
#include <cstring>
using namespace std;

// Length of an unsigned int is usually 4 bytes.

int isDivisibleX(int numb ,int div)
{
	return (numb%div == 0);
}
int main(int argc, char** argv) 
{
    if (argc < 5)
    {
	exit(1);
    }
    unsigned int part1 = atoi(argv[1]);
    unsigned int part2 = atoi(argv[2]);
    unsigned int part3 = atoi(argv[3]);
    unsigned int part4 = atoi(argv[4]);
    unsigned int part5 = 0 ;
    unsigned int part6 = 44 ;
    if (part1 > 0 && part2 > 0 && part3 > 0 && part4 > 0)
    {
	    if (part1+part2 != 96)
		return 1;
	    memcpy(&part5, (&part4),sizeof(unsigned int));
	    part5 >>= 16;
	    if (part5 != 11)
		return 1;
	    part5 += 33;
	    part5 = part5/part6;
	    if (part5 != 1 || ((part5/part6) % part6 != 0) || (part4&0xFFFF) != 1504)    
		return 1;
	    if ((memcmp(&part3,&part2,sizeof(unsigned int)) * part5 * 3) != 0)
	    	return 1;
	    if ((int)part1-(int)part2-(int)part3 < 0 && part2 > 40)
	    {
		for (int i =2; i < 20; i++)
		{
			int res = isDivisibleX(part2, i);
			if (i != 2 && i != 3 && i != 4 && i != 6 && i!= 8 && i != 12 && i != 16)
			{	
				if (res != 0)
				   return 1;
			}
			else
			{
				if (res != 1)
				  return 1;
			}
		}
		printf("Access granted! This is the flag: UHCTF{%d-%d-%d-%d}\n",part1,part2,part3,part4) ;
		return 0;
	    }
	    return 1;
 	
    }
}
