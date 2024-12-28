import Data.Function (on)
import Data.List (groupBy)
import Data.Map qualified as M
import Data.Set qualified as S

type Pos = (Int, Int)

type Grid = [[Char]]

type Antennas = M.Map Char [Pos]

isCollinear :: Pos -> Pos -> Pos -> Bool
isCollinear (x1, y1) (x2, y2) (x3, y3) =
  (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)

parseAntennas :: Grid -> Antennas
parseAntennas grid =
  M.fromListWith
    (++)
    [ (c, [(x, y)])
      | (y, row) <- zip [0 ..] grid,
        (x, c) <- zip [0 ..] row,
        c /= '.'
    ]

pairs :: [a] -> [(a, a)]
pairs xs = [(x, y) | (x : ys) <- tails xs, y <- ys]
  where
    tails [] = []
    tails xs@(_ : rest) = xs : tails rest

findAntinodes :: Grid -> S.Set Pos
findAntinodes grid =
  S.fromList
    [ (x, y)
      | positions <- M.elems (parseAntennas grid),
        x <- [0 .. width - 1],
        y <- [0 .. height - 1],
        any (uncurry (isCollinear (x, y))) (pairs positions)
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