import MancalaBoard
import lab7
import System.IO


isGameOver :: MancalaBoard -> Bool
isGameOver board
	| (canMove board (getCurPlayer board) == []) = True
	| (canMove board (nextPlayer (getCurPlayer) board) == []) = True
	| otherwise = False

endGame :: MancalaBoard -> IO ()
endGame board = do
	putStr "Finish Him, "
	putStr (show $ winners board)
	putStrLn "You are victorious, "
	putStr (show $winners board)

playMancala board = do
					putStrLn (show $ board)
					putStrLn "Choose your tile"
					tile <- getInt
					let tile' = canMove board tile
					case tile' of
						True  -> do
								let board' = move board tile
								nextTurn board'
						False -> do
								putStrLn "Nope.  Do something else.  Please."
								playMancala board

--some helper functions

getInt :: IO Int
getInt = readLn

nextTurn board'
	| gameOver board' == True = endGame board'
	| otherwise = playMancala board'

canMove :: MancalaBoard -> Int -> Bool
canMove board tileNum
	| ((tileNum `elem` (allowedMoves board)) == True) = True
	| otherwise = False

                       
main :: IO()
main = do
	putStrLn "Hey, here's a Mancala game.  "
	let board = initial
	playMancala board
	putStrLn "See you later!"