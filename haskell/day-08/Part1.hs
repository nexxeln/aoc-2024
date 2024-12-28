import Data.Function (on)
import Data.List (groupBy)
import Data.Map qualified as M
import Data.Set qualified as S

type Pos = (Int, Int)

type Grid = [[Char]]

type Antennas = M.Map Char [Pos]

getAntinodes :: Pos -> Pos -> [Pos]
getAntinodes (x1, y1) (x2, y2) =
  [(2 * x2 - x1, 2 * y2 - y1), (2 * x1 - x2, 2 * y1 - y2)]

inBounds :: Int -> Int -> Pos -> Bool
inBounds width height (x, y) = x >= 0 && x < width && y >= 0 && y < height

parseAntennas :: Grid -> Antennas
parseAntennas grid =
  M.fromListWith
    (++)
    [ (c, [(x, y)])
      | (y, row) <- zip [0 ..] grid,
        (x, c) <- zip [0 ..] row,
        c /= '.'
    ]

findAntinodes :: Grid -> S.Set Pos
findAntinodes grid =
  S.fromList
    [ antinode
      | positions <- M.elems (parseAntennas grid),
        (p1, i) <- zip positions [0 ..],
        p2 <- drop (i + 1) positions,
        antinode <- getAntinodes p1 p2,
        inBounds width height antinode
    ]
  where
    height = length grid
    width = length (head grid)

solve :: String -> Int
solve input = S.size $ findAntinodes (lines input)

main :: IO ()
main = do
  contents <- readFile "input.txt"
  print $ solve contents