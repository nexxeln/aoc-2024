import Data.List (nub)

pairs :: [a] -> [(a, a)]
pairs xs = zip xs (tail xs)

differences :: [Int] -> [Int]
differences xs = [b - a | (a, b) <- pairs xs]

allUnique :: [Int] -> Bool
allUnique xs = length (nub xs) == length xs

isMonotonic :: [Int] -> Bool
isMonotonic [] = True
isMonotonic xs = all (> 0) xs || all (< 0) xs

withinBounds :: [Int] -> Bool
withinBounds = all (\x -> abs x >= 1 && abs x <= 3)

isSafe :: [Int] -> Bool
isSafe xs =
  allUnique xs
    && ( let diffs = differences xs
          in isMonotonic diffs && withinBounds diffs
       )

removeAt :: Int -> [a] -> [a]
removeAt i xs = take i xs ++ drop (i + 1) xs

canBeSafe :: [Int] -> Bool
canBeSafe xs = isSafe xs || any isSafe [removeAt i xs | i <- [0 .. length xs - 1]]

main :: IO ()
main = do
  contents <- readFile "input.txt"
  let sequences = [[read x | x <- words line] | line <- lines contents]
  print $ sum [1 | xs <- sequences, canBeSafe xs]