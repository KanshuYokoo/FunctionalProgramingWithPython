module Main where

power :: Int -> Int -> Int
power base exp = base ^ exp

-- Haskell naturally curries functions. We can partially apply by using sections
-- or by passing partial arguments if the parameter order allows.
square :: Int -> Int
square x = power x 2

-- Or using an operator section natively:
square' :: Int -> Int
square' = (^ 2)

cube :: Int -> Int
cube x = power x 3

-- Haskell does not need decorators like lru_cache to cache results if we use lazy evaluation.
-- We can describe the entire infinite series recursively and let Haskell compute on demand.
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Retrieve the nth fibonacci number efficiently
fibonacci :: Int -> Integer
fibonacci n = fibs !! n

main :: IO ()
main = do
    putStrLn $ "Square of 5: " ++ show (square 5)
    putStrLn $ "Cube of 3: " ++ show (cube 3)
    putStrLn $ "50th Fibonacci number: " ++ show (fibonacci 50)
