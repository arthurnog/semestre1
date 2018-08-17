#include <stdio.h>
#include <stdlib.h>

int main() {
  char string[] = "eu sou um bolinho de arroz";
  //26
  for (int i = 0; i < 26; i++) {
    if (string[i] != ' ' && string[i] > 96 && string[i] < 123) {
      string[i] = string[i] + ('A' - 'a');
    }
  }
  printf("%s\n", string);
}
