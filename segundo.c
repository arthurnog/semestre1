#include <stdio.h>

int abs(int a) {
  if (a < 0) {
    return a*-1;
  } else {
    return a;
  }
}
int maior(int a, int b) {
  int maior;
  maior = (a + b + abs(a-b))/2;
  return maior;
}
int main() {
  int a, b, c, result;
  scanf("%d %d %d", &a, &b, &c);
  result = maior(a, b);
  result = maior(result, c);
  printf("%d eh o maior\n", result);
}
