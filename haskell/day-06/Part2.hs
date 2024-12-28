import Data.List (find)
import Data.Map qualified as M
import Data.Maybe (fromJust, isNothing)
import Data.Set qualified as S

type Pos = (Int, Int)

type Grid = M.Map Pos Char

data Dir = North | East | South | West deriving (Eq, Show, Ord)

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

simulateWithObstacle :: Grid -> Pos -> Pos -> Dir -> Pos -> Bool
simulateWithObstacle grid bounds startPos startDir obstacle = go startPos startDir S.empty
  where
    go pos dir seen
      | not (inBounds bounds nextPos) = False
      | nextPos == obstacle || M.lookup nextPos grid == Just '#' =
          let newState = (pos, turnRight dir)
           in newState `S.member` seen || go pos (turnRight dir) (S.insert newState seen)
      | otherwise = go nextPos dir seen
      where
        nextPos = addPos pos (dirToVector dir)

findCandidatePositions :: Grid -> Pos -> Dir -> Pos -> S.Set Pos
findCandidatePositions grid startPos startDir bounds = go startPos startDir S.empty
  where
    go pos dir candidates
      | not (inBounds bounds nextPos) = candidates
      | M.lookup nextPos grid == Just '#' = go pos (turnRight dir) candidates
      | otherwise =
          go
            nextPos
            dir
            ( if isNothing (M.lookup nextPos grid)
                then S.insert nextPos candidates
                else candidates
            )
      where
        nextPos = addPos pos (dirToVector dir)

solve :: Grid -> Int
solve grid =
  length
    [ pos | pos <- S.toList candidates, pos /= startPos, simulateWithObstacle grid bounds startPos startDir pos
    ]
  where
    (startPos, startDir) = findStart grid
    bounds =
      ( maximum [x | (x, _) <- M.keys grid],
        maximum [y | (_, y) <- M.keys grid]
      )
    candidates = findCandidatePositions grid startPos startDir bounds

main :: IO ()
main = do
  contents <- readFile "input.txt"
  print $ solve $ parseGrid contents