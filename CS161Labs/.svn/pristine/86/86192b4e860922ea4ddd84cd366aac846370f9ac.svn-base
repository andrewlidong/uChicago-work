--Andrew Dong Lab 3 derot.  

module Main where

import Data.Char
import Data.List
import System.Environment
import System.IO
import System.Exit

hamming :: [String] -> [String] -> Int
hamming x y = length (intersect x y)

derot :: [String] -> String -> (Int, String)
derot dict file = guess 0 file where
   rotChar n b
      | isLower b = rotCase 'a' b n
      | otherwise = b
   rotCase bs b n = chr (ord bs + (ord b - ord bs + n) 'mod' 26)
   guess n file
      | (n >= 26) = (n, "fail")
      | hamming (take 10 (words (map toLower file))) (dict >= 5) = (n, file)
      | otherwise = guess (n+1)(map ((rotChar (1).toLower) file)
    x dict file = show (fst (derot dict file))
    y dict file = snd (derot dict file)

usage :: IO ()
usage = do
	hPutStrLn stderr $ "Not a sssssssstring! -_-"
	exitWith $ ExitFailure 255

main :: IO ()
main = do
	dictx <- (readFile "/usr/share/dict/words")
	args <- getContents
	putStrLn ((x (lines (map toLower dicta)) args) ++ "=rotation factor")
	putStrLn (y (lines (map toLower dicta)) args)
	
