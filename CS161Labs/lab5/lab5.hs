import Prelude hiding (gcd)
import Data.Char
import Data.List.Split
import Data.Maybe
import Data.Monoid
import System.Environment
import System.IO
import System.Exit

data RArithExpr = Number Int Int | Plus RArithExpr RArithExpr | Mult RArithExpr RArithExpr
	deriving (Show, Eq)

test = test1 && test2
test1 = addition (Number 3 2) (Number 5 4) == (Number 11 4)
test2 = multiplication (Number 3 4) (Number 4 1) == (Number 3 1)


gcd :: Int -> Int -> Int
gcd x 0 = x
gcd 0 x = 0
gcd x 1 = 1
gcd 1 x = flip gcd 1 x
gcd x y = gcd y (x `mod` y)

strParseFraction :: String -> RArithExpr
strParseFraction a = buildRational (read (head b)) (read (last b)) where
	b = splitOneOf "/" (a)

	buildRational :: Int -> Int -> RArithExpr
	buildRational p q = Number (a * b * ((abs p) `div` c)) (abs  q` div` c) where
		a = signum p
		b = signum q
		c = gcd (abs p) (abs q)

addition :: RArithExpr -> RArithExpr -> RArithExpr
addition (Number p q) (Number r s) = Number (numerator `div` c) (denominator `div` c) where
	numerator = p * s + q * r
	denominator = q * s
	c = gcd numerator denominator

multiplication :: RArithExpr -> RArithExpr -> RArithExpr
multiplication (Number p q) (Number r s) = Number (numerator `div` c) (denominator `div` c) where
	numerator = p * r
	denominator = q * s
	c = gcd numerator denominator

data VRArithExpr = Value Int Int [String] | Plusify VRArithExpr VRArithExpr | Multiply VRArithExpr VRArithExpr 
	deriving (Show, Eq)

strParseValue :: String -> VRArithExpr
strParseValue a = concatenate (map buildValue (parseToList (a)))

instance Monoid VRArithExpr where
	mempty = (Value 1 1 [])
	addition <- (Value a b c) `mappend` (Value d e f) = Value (a + d) (b + e) (c ++ f)
	multiplication <- (Value a b c) `mappend` (Value d e f) = Value (a * d `div` (gcd (a * d) (b * e))) (b * e `div` (gcd (a * d) (b * e))) (c ++ f)

concatenate :: [VRArithExpr] -> VRArithExpr
concatenate [] = Value 1 1 []
concatenate (x:xs) = x `mappend` (concatenate xs)

buildValue :: (String, String, String) -> VRArithExpr
buildValue ("","","") = Value 1 1 []
buildValue (a,b,c) = Value (read a) (read b) [c]

parseToList :: [String] -> [(String, String, String)]
parseToList [] = ["1","1", ""]
parseToList (x:xs)
	| stringNumber x = (x, "1", "") : parseToList xs
	| stringVariable x = ("1","1",x) : parseToList xs
	| otherwise = ("1","1","") : parseToList xs

	stringNumber :: String -> Bool
	stringNumber "" = True
	stringNumber (x:xs)
		| isDigit x = True && stringNumber xs
		| otherwise = False

	stringVariable :: String -> Bool
	stringVariable "" = True
	stringVariable (x:xs)
		| isLetter x = True && stringVariable xs
		| otherwise = False





{-eval :: RArithExpr -> Double
eval (Number a) = a
eval (Plus (a) (b)) = eval a + eval b
eval (Mult (a) (b)) = eval a * eval b

simpleParseExpr :: String -> RArithExpr
simpleParseExpr strings = buildExpr (recurse check) where

	check = filter notSpace strings
	notSpace :: Char -> Bool
	notSpace a = not (isSpace a)

	recurse :: String -> [String]
	recurse [] = []
	recurse (x:xs)
		| isDigit x = (takeWhile (isDigit) (x:xs)) : (recurse (dropWhile (isDigit) (x:xs)))
		| x == '-' = ('-':(takeWhile (isDigit) (xs))) : (recurse (dropWhile (isDigit) (xs)))
		| x == '+' || x == '*' = [x]: (recurse xs)
		| otherwise = error "Please try something else.  "

	buildExpr :: [String] -> RArithExpr
	buildExpr list
		| ("+" `elem` list)  = Plus (buildExpr  (fst (break (== "+") list ))) (buildExpr (tail (snd (break (=="+") list)))) 
		| ("*" `elem` list)  = Mult (buildExpr  (fst (break (== "*") list ))) (buildExpr (tail (snd (break (=="*") list)))) 
		| otherwise = Number (read (head list))                     

main :: IO () 
main = do
    putStrLn "We can calculate here: "
    line <- getLine
    putStrLn $ show $ eval (simpleParseExpr line)

    -}