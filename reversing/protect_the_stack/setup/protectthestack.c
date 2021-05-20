#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getflag() {
    const char *s = getenv("CTFFLAG");
    printf("uhctf{%s}\n", (s != NULL) ? s : "NO FLAG FOUND!");
}

int check() {
    char real_password[16];
	char debug_flags[16] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    char password[16];
    printf("Password: ");
	fflush(stdout);
    fgets(password, 32, stdin);
	fflush(stdin);
	password[strcspn(password, "\r\n")] = 0;

	if (debug_flags[0] > 0) {
		printf("ERROR: TAMPERING DETECTED\n");
		return 1;
	}

	strncpy(real_password, getenv("CTFPASSWD"), 16);
	if (debug_flags[4] == 1) {
		printf("DEBUG: %.16s\n", real_password);
	}
	return strncmp(password, real_password, 16);
}

int main() {
    if (check() == 0) {
        getflag();
    } else {
		printf("ERROR: Wrong key!"); 
    }
	fflush(stdout);
    return 0;
}
