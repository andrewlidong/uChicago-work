using System;
using System.Diagnostics;
using System.Collections;
using System.Collections.Generic;

namespace euler {
    class Problem46 {

        public static void Main(string[] args) {                        
            new Problem46().BruteForce();
        }
                
        public void BruteForce() {
            Stopwatch clock = Stopwatch.StartNew();

            int[] primeList = ESieve(10000);

            int result = 1;
            bool notFound = true;
                        
            while(notFound){
                result += 2;
                                                
                int j = 0;
                notFound = false;
                while (result >= primeList[j]) {
                    if(isTwiceSquare(result-primeList[j])){
                        notFound = true;
                        break;
                    }
                    j++;
                }                
            }
                                    
            clock.Stop();
            Console.WriteLine("The smallest counter example is {0}", result);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }


        private bool isTwiceSquare(long number) {
            double squareTest = Math.Sqrt(number/2);
            return squareTest == ((int)squareTest);
        }

        public int[] ESieve(int upperLimit) {

            int sieveBound = (int)(upperLimit - 1) / 2;
            int upperSqrt = ((int)Math.Sqrt(upperLimit) - 1) / 2;

            BitArray PrimeBits = new BitArray(sieveBound + 1, true);

            for (int i = 1; i <= upperSqrt; i++) {
                if (PrimeBits.Get(i)) {
                    for (int j = i * 2 * (i + 1); j <= sieveBound; j += 2 * i + 1) {
                        PrimeBits.Set(j, false);
                    }
                }
            }

            List<int> numbers = new List<int>((int)(upperLimit / (Math.Log(upperLimit) - 1.08366)));
            numbers.Add(2);
            for (int i = 1; i <= sieveBound; i++) {
                if (PrimeBits.Get(i)) {
                    numbers.Add(2 * i + 1);
                }
            }

            return numbers.ToArray();
        }
    }
}
