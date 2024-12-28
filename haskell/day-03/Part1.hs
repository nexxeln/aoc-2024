import Data.Char (isDigit)
import Data.Maybe (catMaybes)
import Text.ParserCombinators.ReadP

number :: ReadP Int
number = do
  digits <- many1 (satisfy isDigit)
  let n = read digits
  if length digits <= 3
    then return n
    else pfail

mulExpr :: ReadP Int
mulExpr = do
  string "mul("
  x <- number
  char ','
  y <- number
  char ')'
  return (x * y)

tryMul :: ReadP (Maybe Int)
tryMul = (Just <$> mulExpr) <++ (Nothing <$ get)

parser :: ReadP [Int]
parser = catMaybes <$> many tryMul

solve :: String -> Int
solve input = sum $ fst $ head $ readP_to_S (parser <* eof) input

main :: IO ()
main = do
  contents <- readFile "input.txt"
  print $ solve contents