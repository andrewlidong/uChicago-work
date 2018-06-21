#include <math.h>
#include <stdio.h>

bool primeCheck(int);
bool goldbachCheck (int);

int main (int argc, char **argv) {
        for (int i = 3; i < 10000; i++) {
                if (i%2==1 && !(primeCheck(i))) {
                        if (!goldbachCheck(i)) printf("%d\n",i);
                }
        }
        return 0;
}

bool primeCheck (int num) {
        if (num<2) return false; 
        else if (num==2 || num==3) return true; 
        else if (num%2==0 || num%3==0) return false; 
        else { 
                int divisor = 5; 
                while (divisor <= sqrt((double)num)) {
                        if (num%divisor==0 || num%(divisor+2)==0) return false;
                        divisor+=6;
                }
        }
        return true;
}

bool goldbachCheck (int num) {
        for (int i = 1; i < num; i++) {
                int square_term = 2*i*i;
                for (int prime = 2; prime <= num - square_term; prime++) {
                        if (primeCheck(prime)) {
                                int potentialValue = prime+square_term;
                                if (potentialValue == num) return true;
                        }
                }
        }
        return false;
}
