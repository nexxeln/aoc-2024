import Data.List (elemIndex, find)

type Rule = (Int, Int)

type Update = [Int]

splitOn :: Char -> String -> [String]
splitOn c s = case break (== c) s of
  (x, []) -> [x]
  (x, _ : xs) -> x : splitOn c xs

parseRule :: String -> Rule
parseRule s = case splitOn '|' s of
  [x, y] -> (read x, read y)
  _ -> error "Invalid rule format"

parseUpdate :: String -> Update
parseUpdate = map read . splitOn ','

parseInput :: String -> ([Rule], [Update])
parseInput input =
  let ls = lines input
      (rules, _ : updates) = break null ls
   in (map parseRule rules, map parseUpdate updates)

followsRule :: Update -> Rule -> Bool
followsRule update (before, after) =
  case (elemIndex before update, elemIndex after update) of
    (Just i, Just j) -> i < j
    _ -> True

isValidUpdate :: [Rule] -> Update -> Bool
isValidUpdate rules update = all (followsRule update) rules

middle :: [a] -> a
middle xs = xs !! (length xs `div` 2)

solve :: String -> Int
solve input =
  let (rules, updates) = parseInput input
      validUpdates = filter (isValidUpdate rules) updates
   in sum $ map middle validUpdates

main :: IO ()
main = do
  contents <- readFile "input.txt"
  print $ solve contents