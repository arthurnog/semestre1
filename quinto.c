#include <stdio.h>
#include <string.h>

char toLowercase(char a) {
  if (a >= 'A' && a <='Z') {
    return a + ('a' - 'A');
  }
  return a;
}

int main() {
  char frase[] = "Babuinos bobocas bAlBuCiAnDo em Bando";
  char primeira = toLowercase(frase[0]);
  int anterior_espaco = 0;
  for (int i = 0; i < strlen(frase); i++) {
    if (frase[i] == ' ') {
      anterior_espaco = 1;
    } else if (anterior_espaco) {
      if(toLowercase(frase[i]) != primeira) {
        printf("N\n");
        return 0;
      }
      anterior_espaco = 0;
    }
  }
  printf("S\n");
}
