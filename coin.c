#include <stdio.h>
#include <conio.h>
int main()
{
    int amount,temp,coin[10],count,coincount=0;
    printf("Enter the amount:");
    scanf("%d",&amount);
    printf("enter the count of coins:");
    scanf("%d",&count);
    for(int i=0;i<count;i++){
        scanf("%d",&coin[i]);
    }

    /*Sorting*/

    for (int i = 0; i < count; i++)
    {
        for(int j = 0; j < count; j++){
            if(coin[j] < coin[i]){
                temp = coin[i];
                coin[i] = coin[j];
                coin[j] = temp;
            }
        }
    }

     for(int i=0;amount!=0;i++){ 
        printf("%d * %d = %d\n",coin[i],amount/coin[i],amount/coin[i]*coin[i]);
        coincount+=amount/coin[i];
        amount%=coin[i];
        
     
    }
     printf("%d coin used \n",coincount);
}
