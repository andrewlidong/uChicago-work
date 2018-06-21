module MancalaAI(aiNextMove) where

import MancalaBoard
import Data.List
import Data.Maybe

type Move = Int

playerA = allPlayers !! 0
playerB = allPlayers !! 1

aiNextMove :: MancalaBoard -> Move
aiNextMove mancala = lookahead mancala 0

evalPosition :: Int -> MancalaBoard -> Int

evalPosition 0 mancala = (multiply $ numCaptured mancala player) + (numTotal mancala) - (multiply $ numCaptured mancala next) + canMoveAgain where
			player = getCurPlayer mancala
			next
				| player == playerA = playerB
				| player == playerB = playerA
			canMoveAgain = (length $ goAgainCount player moveList) - (length $ goAgainCount next moveList)
			moveList = map (move mancala) (allowedMoves mancala)
			numTotal a = sum $ map (getBoardData a !!) (allowedMoves a)
			multiply a
				| a < 10 = (10 - a) * a
				|otherwise = 2 * a

evalPosition depth mancala = 
			if (endGame mancala)
				then
					evalPosition 0 mancala
				else
					iter * (evalPosition (depth -1) newMancala) where
				endGame mancala = null $ allowedMoves mancala
				newMancala = move mancala newMove
				newMove = lookahead mancala (depth - 1)
				iter
					| getCurPlayer mancala == getCurPlayer newMancala = 1
					| otherwise = -1

lookahead :: MancalaBoard -> Int -> Move
lookahead mancala depth = (allowedMoves mancala) !! foundMove where
			foundMove = 
				if (goAgain (current) moveList)
					then 
						found $ elemIndex (getBoardData (last (goAgainCount current moveList))) moveListBoard
					else
						last $ elemIndices topMove moveResults
			current = getCurPlayer mancala			
			topMove = last $ sort $ moveResults
			am = allowedMoves mancala
			am2
				| length am > 1 = delete topNum am
				| otherwise = am
			moveResults = map (evalPosition depth) moveList
			moveList = map (move mancala) am2
			moveListBoard = map getBoardData moveList
			bd = getBoardData mancala
			moveNums = map (bd !!) am
			topNum = am !! (found $ elemIndex (head $ sort moveNums) moveNums )
			found m
				| isJust m = fromJust m
				| otherwise = 0
				

goAgain :: Player -> [MancalaBoard] -> Bool
goAgain p movelist = or (map ((== p) . getCurPlayer) movelist)

goAgainCount :: Player -> [MancalaBoard] -> [MancalaBoard]
goAgainCount p movelist = filter ((==p) . getCurPlayer) movelist

