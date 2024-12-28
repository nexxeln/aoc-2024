import Data.List (find)
import Data.Map qualified as M
import Data.Maybe (fromJust)

type Pos = (Int, Int)

type Grid = M.Map Pos Char

data Dir = North | East | South | West deriving (Eq, Show)

charToDir :: Char -> Dir
charToDir '^' = North
charToDir '>' = East
charToDir 'v' = South
charToDir '<' = West

dirToVector :: Dir -> Pos
dirToVector North = (0, -1)
dirToVector East = (1, 0)
dirToVector South = (0, 1)
dirToVector West = (-1, 0)

turnRight :: Dir -> Dir
turnRight North = East
turnRight East = South
turnRight South = West
turnRight West = North

addPos :: Pos -> Pos -> Pos
addPos (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)

inBounds :: Pos -> Pos -> Bool
inBounds (maxX, maxY) (x, y) = x >= 0 && y >= 0 && x <= maxX && y <= maxY

parseGrid :: String -> Grid
parseGrid input =
  M.fromList
    [ ((x, y), c) | (y, row) <- zip [0 ..] (lines input), (x, c) <- zip [0 ..] row, c `elem` "^v<>#"
    ]

findStart :: Grid -> (Pos, Dir)
findStart grid = (pos, charToDir dir)
  where
    (pos, dir) = fromJust $ find ((`elem` "^v<>") . snd) $ M.toList grid

simulate :: Grid -> Int
simulate grid = length $ go startPos startDir M.empty
  where
    (startPos, startDir) = findStart grid
    bounds = (maximum [x | (x, _) <- M.keys grid], maximum [y | (_, y) <- M.keys grid])

    go pos dir visited
      | not (inBounds bounds nextPos) = visited'
      | M.lookup nextPos grid == Just '#' = go pos (turnRight dir) visited'
      | otherwise = go nextPos dir visited'
      where
        nextPos = addPos pos (dirToVector dir)
        visited' = M.insert pos '#' visited

main :: IO ()
main = do
  contents <- readFile "input.txt"
  print $ simulate $ parseGrid contents
