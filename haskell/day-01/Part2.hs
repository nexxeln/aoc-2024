import Data.List (group, sort)

solve :: [(Int, Int)] -> Int
solve pairs = sum [l * length (filter (== l) rights) | l <- lefts]
  where
    lefts = [l | (l, _) <- pairs]
    rights = [r | (_, r) <- pairs]

main :: IO ()
main = do
  contents <- readFile "input.txt"
  let pairs = [(read l, read r) | [l, r] <- map words (lines contents)]
  print (solve pairs)