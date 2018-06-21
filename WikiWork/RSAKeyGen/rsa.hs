--Andrew Dong
--RSA Key Generator


module Main where

import System.Environment
import Data.List

keyGenerator :: Integer -> Integer -> ((Integer, Integer), (Integer, Integer))
keyGenerator a b = ((n, e), (n, d)) where
    n = a * b
    t = (a - 1) * (b - 1)
    e = coprimeFinder t
    d = modularMultiplicativeInverseFinder e t

coprimeFinder :: Integer -> Integer
coprimeFinder t = e where
    esieve (primenum : nums) = primenum : esieve [primes | primes <- nums, 
                                        primes `mod` primenum > 0]

    listofprimes = esieve [2..]

    e = head $ dropWhile (< 2^10) (filter (\x -> mod t x /= 0) listofprimes)


modularMultiplicativeInverseFinder = modularInverse

gcdFinder a 0 = (1, 0, a)
gcdFinder a b = let (q, r) = a `quotRem` b
                    (s, t, g) = gcdFinder b r
             in (t, s - q * t, g)

modularInverse a m = 
			let (i, _, g) = gcdFinder a m
             in (makePositive i) 
  where makePositive x = 
				if x < 0 
				then x + m 
				else x

main :: IO ()
main = do
    args <- getArgs
    case args of
        [primeA, primeB] -> if primeA /= primeB
                                    then do
                                            let (pubkey, privkey) = keyGenerator (read primeA) (read primeB)
                                            print $ "PUBLIC KEY =  " ++ show pubkey
                                            print $ "PRIVATE KEY =  " ++ show privkey
                                    else do
                                        print "The two prime number arguments must be distinct."
        _ -> do
            print "Please insert two prime numbers as arguments when compiling."   
