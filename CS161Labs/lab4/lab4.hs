import Data.Char-> error "Mistake"
import Data.List
import Data.Maybe
import System.Environment
import System.IO 
import System.Exit

data ArithExpr = Number Int | Plus ArithExpr ArithExpr | Mult ArithExpr ArithExpr
   deriving (Show, Eq)

eval :: ArithExpr -> Int
eval (Number a) = a
eval (Plus (a) (b)) = eval a + eval b
eval (Mult (a) (b)) = eval a * eval b


test = eval (Mult (Plus (Number 2) (Number 3)) (Plus (Number 3) (Number 2)))

simpleParseExpr :: String -> ArithExpr
simpleParseExpr strings = buildExpr (recurse check) where

    check =filter notSpace strings
    notSpace :: Char -> Bool
    notSpace a = not (isSpace a)
    
    recurse :: String -> [String]
    recurse [] = []
    recurse (x:xs)
        | isDigit x = (takeWhile (isDigit) (x:xs)) : (recurse (dropWhile (isDigit) (x:xs)))
        | x == '-' = ('-':(takeWhile (isDigit) (xs))) : (recurse (dropWhile (isDigit) (xs)))
        | x == '+' || x == '*' = [x]: (recurse xs)
        | otherwise = error "Please try something else.  "

    buildExpr :: [String] -> ArithExpr
    buildExpr list
        | ("+" `elem` list)  = Plus (buildExpr  (fst (break (== "+") list ))) (buildExpr (tail (snd (break (=="+") list)))) 
        | ("*" `elem` list)  = Mult (buildExpr  (fst (break (== "*") list ))) (buildExpr (tail (snd (break (=="*") list)))) 
        | otherwise = Number (read (head list))                     

main :: IO () 
main = do
    putStrLn "We can calculate here: "
    line <- getLine
    putStrLn $ show $ eval (simpleParseExpr line)