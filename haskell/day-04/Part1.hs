import Data.List (transpose)

type Grid = [[Char]]

type Pos = (Int, Int)

type Dir = (Int, Int)

getWord :: Grid -> Pos -> Dir -> Int -> Maybe String
getWord grid (i, j) (di, dj) len =
  if all inBounds [(i + di * k, j + dj * k) | k <- [0 .. len - 1]]
    then Just [grid !! (i + di * k) !! (j + dj * k) | k <- [0 .. len - 1]]
    else Nothing
  where
    rows = length grid
    cols = length (head grid)
    inBounds (x, y) = x >= 0 && x < rows && y >= 0 && y < cols

isMatch :: String -> String -> Bool
isMatch word target = word == target || reverse word == target

countXMAS :: Grid -> Int
countXMAS grid =
  sum
    [ 1 | i <- [0 .. rows - 1], j <- [0 .. cols - 1], dir <- [(0, 1), (1, 1), (1, 0), (1, -1)], Just word <- [getWord grid (i, j) dir 4], isMatch word "XMAS"
    ]
  where
    rows = length grid
    cols = length (head grid)

main :: IO ()
main = do
  contents <- readFile "input.txt"
  let grid = lines contents
  print $ countXMAS grid