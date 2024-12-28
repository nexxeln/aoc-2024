type Op = Int -> Int -> Int

type Equation = (Int, [Int])

operators :: [Op]
operators = [(+), (*)]

combinations :: Int -> [[Op]]
combinations 0 = [[]]
combinations n = [op : rest | op <- operators, rest <- combinations (n - 1)]

evaluate :: [Int] -> [Op] -> Int
evaluate (x : xs) ops = foldl (\acc (op, y) -> op acc y) x (zip ops xs)

canSolve :: Equation -> Bool
canSolve (target, nums) = any ((== target) . evaluate nums) (combinations (length nums - 1))

parseEquation :: String -> Equation
parseEquation line = case break (== ':') line of
  (test, _ : rest) -> (read test, map read $ words rest)

solve :: String -> Int
solve input = sum [target | eq@(target, _) <- equations, canSolve eq]
  where
    equations = map parseEquation $ lines input

main :: IO ()
main = do
  contents <- readFile "input.txt"
  print $ solve contents