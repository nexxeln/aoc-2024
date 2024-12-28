import Text.ParserCombinators.ReadP
import Data.Char (isDigit)
import Data.Maybe (catMaybes)

data Instruction = Mul Int Int | Do | Dont
    deriving Show

number :: ReadP Int
number = do
    digits <- many1 (satisfy isDigit)
    let n = read digits
    if length digits <= 3 
        then return n
        else pfail

mulExpr :: ReadP Instruction
mulExpr = do
    string "mul("
    x <- number
    char ','
    y <- number
    char ')'
    return (Mul x y)

doExpr :: ReadP Instruction
doExpr = (Do <$ string "do()") <++ (Dont <$ string "don't()")

tryInstruction :: ReadP (Maybe Instruction)
tryInstruction = (Just <$> (mulExpr <++ doExpr)) <++ (Nothing <$ get)

parser :: ReadP [Instruction]
parser = catMaybes <$> many tryInstruction

processInstructions :: [Instruction] -> Int
processInstructions = go True 0
  where
    go _ acc [] = acc
    go enabled acc (instr:rest) = case instr of
        Mul x y -> go enabled (if enabled then acc + x * y else acc) rest
        Do -> go True acc rest
        Dont -> go False acc rest

solve :: String -> Int
solve input = processInstructions $ fst $ head $ readP_to_S (parser <* eof) input

main :: IO ()
main = do
    contents <- readFile "input.txt"
    print $ solve contents