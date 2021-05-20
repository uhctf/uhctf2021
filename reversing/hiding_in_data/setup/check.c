#include <stdio.h>
#include <stdlib.h>

int check(int x, int y, int z, int w) {
	if (x == 39292 && y == 18012 && z == 40581 && w == 42374) {
		return 1;
		// printf("uhctf{%04x-%04x-%04x-%04x}\n", x, y, z, w);
	} else {
		return 0;
		// printf("Wrong key!\n");
	}
}

int main(int argc, char **argv) {
    int x = atoi(argv[1]), y = atoi(argv[2]), z = atoi(argv[3]),
        w = atoi(argv[4]);
	if (check(x, y, z, w)) {
		printf("uhctf{%04x-%04x-%04x-%04x}\n", x, y, z, w);
	}
	return 0;
}
