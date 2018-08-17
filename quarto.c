#include <stdio.h>
#include <stdlib.h>

int main() {
  char frase[] = "Noites em claro e lolo";
  // 22 characteres
  //saida = NoItEs Em ClArO e LoLo
  for (int i = 0; i < 22; i++) {
    if (frase[i] != ' ' && frase[i] > 96 && frase[i] < 123 && i % 2 == 0) {
      frase[i] = frase[i] + ('A' - 'a');
    }
  }
  printf("%s\n", frase);
}
