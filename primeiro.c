#include <stdio.h>

int main() {
  float tot = 0.0;
  int codigo = 0;
  int quantidade = 0;
  float preco = 0.0;
  float total = 0.0;
  int codigo2 = 0;
  int quantidade2 = 0;
  float preco2 = 0.0;
  float total2 = 0.0;
  scanf("%d %d %f", &codigo, &quantidade, &preco);
  scanf("%d %d %f", &codigo2, &quantidade2, &preco2);
  total = (float) preco*quantidade;
  total2 = (float) preco2*quantidade2;
  tot = total + total2;
  printf("VALOR A PAGAR: R$ %.2f\n", tot);
}
