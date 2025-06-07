#include <stdio.h>
#include <string.h>

void secret_function() {
    printf("You have successfully triggered the secret function!\n");
}

void vulnerable_function(char *input) {
    char buffer[64];
    strcpy(buffer, input);  // Utilisation de strcpy() vulnérable
    printf("You entered: %s\n", buffer);  // Affiche la chaîne copiée dans le buffer
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <input_string>\n", argv[0]);
        return 1;
    }
    
    vulnerable_function(argv[1]);
    printf("Program finished executing.\n");
    return 0;
}
