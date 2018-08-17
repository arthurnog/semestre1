#include <stdio.h>


typedef struct{
	int n;
	float multi;
}pokemon;

int main(){
	pokemon entrada[152];
	int n,aux;
	float pca,pcf;
	int pc;
	float temp;
	scanf("%d",&n);
	for(int i=0;i<152;i++){	
		entrada[i].multi = 0;
		entrada[i].n = 0;
	}
	for(int i=0;i<n;i++){
		scanf("%d",&aux);
		scanf("%f",&pca);
		scanf("%f",&pcf);
		entrada[aux].multi = pcf/pca + entrada[aux].multi;
		entrada[aux].n++;
	}
	for(int i=0;i<152;i++){
		if(entrada[i].n != 0){	
			entrada[i].multi = entrada[i].multi/entrada[i].n;
		}
	}
	scanf("%d",&aux);
	scanf("%d",&pc);
	while((aux!=0) || (pc!=0)){
		temp = pc*entrada[aux].multi;
		n = pc*entrada[aux].multi;
		if ((temp-n)>0){
			n = n+1;
		}
		printf("%d \n",n);
		scanf("%d",&aux);
		scanf("%d",&pc);
	}
	return 0;
} 		
