import Data.List (sort)

solve :: [(Int, Int)] -> Int
solve pairs = sum [abs (a - b) | (a, b) <- zip lefts rights]
  where
    lefts = sort [l | (l, _) <- pairs]
    rights = sort [r | (_, r) <- pairs]

main :: IO ()
main = do
    contents <- readFile "input.txt"
    let pairs = [(read l, read r) | [l, r] <- map words (lines contents)]
    print (solve pairs) 