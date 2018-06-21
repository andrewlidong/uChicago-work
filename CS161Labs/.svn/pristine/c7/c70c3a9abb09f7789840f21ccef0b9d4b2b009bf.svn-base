import StateExample
import RandState
import UCState
import System.Random
import Control.Monad
import Data.List

{-Exercise 1: testStateExample2 tests that the list output by stateExample2 is the correct length-}
testStateExample2 :: IO Bool
testStateExample2 = do
	list <- stateExample2 3
	let a = length list
	return (a == 3)

{-Exercise 2: testAll tests everything and includes the number of tests passed-}
testAll :: IO String
testAll = do
	let tests = [testStateExample2, randRTest]
	number <- (testsPassed tests)
	return $ (show number) ++ " tests out of " ++ (show $ length tests) ++ " tests got passed.  Balling!"
	where
		testsPassed :: [IO (Bool)] -> IO (Int)
		testsPassed [] = return 0
		testsPassed (x:xs) = do
			b <- x
			if b
				then fmap (+1) (testsPassed xs)
			else testsPassed xs


{-Exercise 3: randR is like rand, but generates numbers in a specific range.  -}
randR :: Random a => (a,a) -> RandState a
randR (a,b) = do
	gen <- get 
	let (x, gen') = randomR (a,b) gen
	put gen'
	return x

{-randRTest tests whether the value for randR falls between 0 and 1000, which it should (and it does!)-}
randRTest :: IO Bool
randRTest = do
	g <- newStdGen
	let a = runRandom (randR (0,1000)) g:: Double
	return (a >= 0 && a <=1000)



{-Exercise 4: rollTwoDice generates a random sum of two dice (between 2 and 12)-}

rollTwoDice :: RandState Int
rollTwoDice = do
	dice1 <- (randR (1,6))
	dice2 <- (randR (1,6))
	return (dice1 + dice2)

{-rollTwoDiceTest :: IO Bool
rollTwoDiceTest = do
	g <- newStdGen
	let 

I'm not currently able to get rollTwoDiceTest to work.  
I know that rollTwoDiceTest should run multiple times and output numbers between 2 and 12.  
The probability of landing should be something like
[1/36, 1/18, 1/12, 1/9, 5/36, 1/6, 5/36, 1/9, 1/12, 1/18, 1/36], 
so I"ll have to compare actual values (over many runs) with these values.  
So I'll have to create another function that determies whether the actual values
are sufficiently close (setting delta small)

-}


data CardValue = King | Queen | Jack | NumberCard Int
	deriving (Show, Eq)
data CardSuit = Hearts | Diamonds | Spades | Clubs
	deriving (Show, Eq)
data PlayingCard = PlayingCard CardSuit CardValue
	deriving (Show, Eq)

fullCardDeck :: [PlayingCard]
fullCardDeck = [PlayingCard s v | s <- allsuits, v <- allvals] where
	allvals = King : Queen : Jack : [ NumberCard i | i <- [1..10] ]
	allsuits = [Hearts, Diamonds, Spades, Clubs]

{-Exercise 5: removeCard is monadic, and picks a random card out of a list, returns that card and the list with the card removed-}
removeCard :: [PlayingCard] -> RandState (PlayingCard , [PlayingCard])
removeCard deck = do
	index <- randR (0, (length deck) -1)
	let a = deck !! index
	return (a, delete a deck) -- lol
{-
removeCardTest :: IO Bool
removeCardTest = do
	g <- newStdGen
-}

{-Exercise 6: shuffleDeck takes a list of playing cards and then returns random permutations-}
shuffleDeck:: [PlayingCard] -> RandState [PlayingCard]
shuffleDeck deck = recurse deck where
	recurse deck = do 
		if (length deck) > 0
			then do
				(x,y) <- removeCard deck
				z <- recurse y
				return (x:z)
		else return []

{-Exercise 7: shuffleADeck generates and outputs a shuffle of 52 cards-}
shuffleADeck:: RandState [PlayingCard]
shuffleADeck = shuffleDeck fullCardDeck

{-Exercise 8: approxPi will approximate pi using Monte Carlo method-}
piTrial :: RandState Bool
piTrial = do
	x <- (randR (-1.0, 1.0 :: Double))
	y <- (randR (-1.0, 1.0 :: Double))
	return ((x**2 + y**2) <= 1)

bernoulliTrials :: Int -> RandState Bool -> RandState Int
bernoulliTrials n f = recurse n where
	recurse a = do
		if a > 0
			then do
				b <- f
				case b of
					False -> do
						c <- recurse (a-1)
						return c
					True -> do
						c <- recurse (a-1)
						return (1+c)
		else return 0

approxPi :: Int -> RandState Double
approxPi n = do
	a <- bernoulliTrials n piTrial
	return (4 * (fromIntegral a)/(fromIntegral n))
