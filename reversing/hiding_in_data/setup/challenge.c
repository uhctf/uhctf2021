#include <malloc.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <unistd.h>

static char *magicbuffer;

const uint8_t keychecker[66] = {
    0x55, 0x48, 0x89, 0xE5, 0x89, 0x7D, 0xFC, 0x89, 0x75, 0xF8, 0x89,
    0x55, 0xF4, 0x89, 0x4D, 0xF0, 0x81, 0x7D, 0xFC, 0x7C, 0x99, 0x00,
    0x00, 0x75, 0x22, 0x81, 0x7D, 0xF8, 0x5C, 0x46, 0x00, 0x00, 0x75,
    0x19, 0x81, 0x7D, 0xF4, 0x85, 0x9E, 0x00, 0x00, 0x75, 0x10, 0x81,
    0x7D, 0xF0, 0x86, 0xA5, 0x00, 0x00, 0x75, 0x07, 0xB8, 0x01, 0x00,
    0x00, 0x00, 0xEB, 0x05, 0xB8, 0x00, 0x00, 0x00, 0x00, 0x5D, 0xC3};

int main(int argc, char **argv) {
    int pagesize;
    if (argc != 5) {
        printf("Use the four keys as parameters to gain access.\n");
        printf("Example: ./challenge 1 2 3 4\n");
        return 0;
    }

    pagesize = sysconf(_SC_PAGE_SIZE);
    magicbuffer = (char *)memalign(pagesize, 1 * pagesize);
    mprotect(magicbuffer, pagesize, PROT_READ | PROT_WRITE | PROT_EXEC);
    memcpy(magicbuffer, keychecker, 66);
    int (*func)(int, int, int, int) = (int (*)(int, int, int, int))magicbuffer;
    int x = atoi(argv[1]), y = atoi(argv[2]), z = atoi(argv[3]),
        w = atoi(argv[4]);
    if (func(x, y, z, w)) {
        printf("uhctf{%04x-%04x-%04x-%04x}\n", x, y, z, w);
    } else {
        printf("Wrong keys\n");
    }
}
