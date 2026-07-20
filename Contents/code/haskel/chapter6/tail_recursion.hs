module TailRecursion where

-- 1. Factorial: Non-Tail Recursive
-- GHC cannot optimize this, as multiplication by n must happen after
-- factorialRecursive (n - 1) returns.
factorialRecursive :: Integer -> Integer
factorialRecursive 0 = 1
factorialRecursive n = n * factorialRecursive (n - 1)


-- 2. Factorial: Tail Recursive (Accumulator Pattern)
-- The recursive call is GHC's final operation in the function.
-- GHC optimizes this into an iterative loop.
factorialTailRecursive :: Integer -> Integer
factorialTailRecursive n = go n 1
  where
    go :: Integer -> Integer -> Integer
    go 0 acc = acc
    go x acc = go (x - 1) (x * acc)


-- 3. Greatest Common Divisor (GCD): Naturally Tail Recursive
-- Euclid's algorithm naturally puts the recursive call in the tail position.
-- No accumulator helper is necessary.
gcdEuclid :: Integer -> Integer -> Integer
gcdEuclid a 0 = a
gcdEuclid a b = gcdEuclid b (a `mod` b)


main :: IO ()
main = do
    putStrLn $ "factorialRecursive 5 = " ++ show (factorialRecursive 5)
    putStrLn $ "factorialTailRecursive 5 = " ++ show (factorialTailRecursive 5)
    putStrLn $ "gcdEuclid 48 18 = " ++ show (gcdEuclid 48 18)
