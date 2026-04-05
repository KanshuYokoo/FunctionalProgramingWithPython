-- Haskell has native support for proving laws using QuickCheck, 
-- but here we write simple assertions to understand the concept.

-- Testing Applicative: <*>
boxFunc :: Maybe (Int -> Int)
boxFunc = Just (* 10)

boxVal :: Maybe Int
boxVal = Just 5

applicativeResult :: Maybe Int
applicativeResult = boxFunc <*> boxVal 
-- Evaluates to Just 50

-- Monad Laws:
-- 1. Left Identity: return x >>= f == f x
leftId :: Bool
leftId = (return 5 >>= \x -> Just (show x)) == (\x -> Just (show x)) 5

-- 2. Right Identity: m >>= return == m
rightId :: Bool
rightId = (Just 5 >>= return) == Just 5

-- 3. Associativity: (m >>= f) >>= g == m >>= (\x -> f x >>= g)
assoc :: Bool
assoc = ((Just 5 >>= \x -> Just (x * 2)) >>= \y -> Just (show y)) 
     == (Just 5 >>= \x -> (\y -> Just (show y)) (x * 2))

main :: IO ()
main = do
    putStrLn $ "Applicative Result: " ++ show applicativeResult
    putStrLn $ "Left Identity: " ++ show leftId
    putStrLn $ "Right Identity: " ++ show rightId
    putStrLn $ "Associativity: " ++ show assoc
