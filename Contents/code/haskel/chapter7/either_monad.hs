-- In Haskell, Either is defined as: data Either a b = Left a | Right b
-- It is natively a Monad where Right is success and Left is failure.

divideBy :: Int -> Int -> Either String Int
divideBy 0 _ = Left "Cannot divide by zero"
divideBy y x = Right (x `div` y)

-- Using the bind operator (>>=)
successChain :: Either String Int
successChain = Right 100 >>= divideBy 2 >>= divideBy 5
-- Result: Right 10

failChain :: Either String Int
failChain = Right 100 >>= divideBy 0 >>= divideBy 5
-- Result: Left "Cannot divide by zero"

-- Using do-notation
doChain :: Either String Int
doChain = do
    x <- Right 100
    y <- divideBy 2 x
    divideBy 5 y

main :: IO ()
main = do
    print successChain
    print failChain
    print doChain
