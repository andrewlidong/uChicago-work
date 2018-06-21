--Andrew Dong Lab 3 vindecoden.  

module Main where

import Data.Char
import Data.List
import System.Environment
import System.IO
import System.Exit

data Tree = Leaf Int | Node Int Tree Tree deriving (Show, Eq) 

initTree :: Int -> initTree
initTree n
   | (n == 0) = Leaf 0
   | otherwise = Node n (initTree (n-1))(initTree (n-1))

whichBranch :: Int -> Tree -> Tree
whichBranch a (Node x y z)
   | (b < 0) = y
   | (b >= 0) = z

treeCountx :: Tree -> Int -> Int
treeCountx (Leaf x) a = x
treeCount b@(Node x y z) a
   | (a > 2^(c-1)) = undefined
   | otherwise = treeCountx (whichBranch(a - 2^(c-1) b)(mod a (2^(x-1)))
treeCount tree a = treeCountx tree(a+1)

treeInsert :: Int-> Tree -> Tree
treeInsertx a (Leaf x) = Leaf (x+1)
treeInserta a b@(Node x y z)
    | (a > 2^x) = undefined
    | (a - 2^(x-1) >= 0) = Node x y (treeInsertx (mod a (2^(x-1))) z)
    | (a - 2^(x-1) < 0)  = Node x (treeInserta (mod a (2^(x-1))) y) z
treeInsert a = treeInsertx (a+1)

asciitreeinsert :: Tree -> Char -> Tree