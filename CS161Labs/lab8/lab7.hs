module MancalaBoard (MancalaBoard, Player, initial, getCurPlayer, getBoardData, numCaptured, move, allowedMoves, isAllowedMove, gameOver, winners) where

import Data.List as List 
import Data.Maybe as Maybe 
import System.IO

            
test :: MancalaBoard -> Bool
test board
    |(getCurPlayer board == PlayerA) 
		&& (getBoardData board == [4,4,4,4,4,4,0,4,4,4,4,4,4,0]) 
		&& (playerSide board == [0,1,2,3,4,5,6]) 
		&& (numCaptured board PlayerA == 0) 
		&& (allowedMoves board == [1,2,3,4,5]) 
		&& (isAllowedMove board 6 == True) 
		&& (isAllowedMove board 0 == False) 
		&& (gameOver board == False) 
		&& (getBoardData (move initial 3) == [4,4,4,0,5,5,1,5,4,4,4,4,4,0])
		 = True
    |otherwise = False
    

data MancalaBoard = MancalaBoardImpl [Int] Player

data Player = PlayerA | PlayerB deriving (Eq, Show)

allPlayers = [PlayerA, PlayerB]
numPlayers = length allPlayers

playerNum :: Player -> Int
playerNum p = fromJust $ List.elemIndex p allPlayers

playerWithNum :: Int -> Player
playerWithNum i = allPlayers !! i

nextPlayer :: Player -> Player
nextPlayer p = playerWithNum $ ((playerNum p) + 1) `mod` numPlayers

boardSize = 6
startStones = 4

initial :: MancalaBoard
initial = MancalaBoardImpl (concat $ take numPlayers (repeat boardSide)) PlayerA
    where boardSide = take boardSize (repeat startStones) ++ [0]

indexForFirstPit :: Player -> Int
indexForFirstPit p = (playerNum p) * (boardSize + 1)

indexForPlayerStore :: Player -> Int
indexForPlayerStore p = boardSize + (indexForFirstPit p)

indicesForPlayerSide :: Player -> [Int]
indicesForPlayerSide p = [firstPit .. lastPit] where
    firstPit = indexForFirstPit p
    lastPit = firstPit + boardSize - 1

getCurPlayer :: MancalaBoard -> Player
getCurPlayer (MancalaBoardImpl list player) = player

getBoardData :: MancalaBoard -> [Int]
getBoardData (MancalaBoardImpl list player) = list

playerSide :: MancalaBoard  -> [Int]
playerSide board = (indicesForPlayerSide (getCurPlayer board)) ++ ((indexForPlayerStore (getCurPlayer board)):[])

numCaptured :: MancalaBoard -> Player -> Int
numCaptured board player = (getBoardData board) !! (indexForPlayerStore player)

allowedMoves :: MancalaBoard -> [Int]
allowedMoves board = possibleMove 0 [] where
	possibleMove 6 y = reverse y
	possibleMove x y
		| ((playerSide board !! x) == 0) = possibleMove (x+1) y
		| otherwise = possibleMove (x+1) (x:y)

isAllowedMove :: MancalaBoard -> Int -> Bool
isAllowedMove board tileNum
	| ((tileNum `elem` (allowedMoves board)) == True) = True
	| otherwise = False

move :: MancalaBoard -> Int -> MancalaBoard
move board i = MancalaBoardImpl newBoard newPlayer where
                     board2 = fst (moveStones (getBoardData board) i)
                     newPlayer = 
								if ((i + (getBoardData board) !! i) == indexForPlayerStore (getCurPlayer board)) 
									then (getCurPlayer board)
                                else (nextPlayer (getCurPlayer board))
                     newBoard = 
								if (isAllowedMove board i == True) 
									then (movepit board2 ((getBoardData board) !! i) ((i+1) `mod` (length (getBoardData board))) (indexForPlayerStore (nextPlayer (getCurPlayer board)))) 
                                else (error "this move is not allowed")
														
moveStones board 0 = ((0 : (tail board)), head board)
moveStones board i = ((( head board) : (fst locationi)), snd locationi) where 
								locationi = moveStones (tail board) (i-1)
								
movepit board 0 x y = board
movepit board stones i store
    | i == store = movepit board stones ((i+1) `mod` (length board)) store
    | otherwise = movepit (boardShift board i) (stones -1) ((i+1) `mod` (length board)) store 
    
boardShift board i 
    | i> length board = boardShift board (i `mod` length board)
    | i == 0 = (( head board +1) : (tail board))
    | otherwise = ((head board) : (boardShift (tail board) (i-1)))

gameOver :: MancalaBoard -> Bool
gameOver (MancalaBoardImpl list player)
    | (allowedMoves (MancalaBoardImpl list player) /= []) = False
    | (allowedMoves (MancalaBoardImpl list (nextPlayer player)) /= []) = False
    | otherwise = True 

winners :: MancalaBoard -> [Player]
winners board 
    | (numCaptured board PlayerA > numCaptured board PlayerB) = [PlayerA]
    | (numCaptured board PlayerA < numCaptured board PlayerB) = [PlayerB]
    | (numCaptured board PlayerA == numCaptured board PlayerB) = allPlayers

instance Show MancalaBoard where
    show (MancalaBoardImpl boardData player) =
            (show (take 7 boardData)) ++ " " ++ (show player) ++ "\n"++ (show (drop 7boardData)) ++ " " ++ (show (nextPlayer player))

