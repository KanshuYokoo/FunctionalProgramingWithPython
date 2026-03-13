module IterationRecursion where

-- 1. Recursion: The only way to loop
-- Unlike Python, Haskell has no 'for' or 'while' loops.
-- Recursion is the standard way to repeat operations.

-- We define recursion using pattern matching.
sumRecursive :: Int -> Int
sumRecursive 0 = 0                      -- Base case
sumRecursive n = n + sumRecursive (n - 1) -- Recursive step

-- Or using Guard clauses for another style
sumRecursiveGuards :: Int -> Int
sumRecursiveGuards n
    | n <= 0    = 0
    | otherwise = n + sumRecursiveGuards (n - 1)


-- 2. Tail Call Optimization (TCO)
-- The above `sumRecursive` builds a big call stack: 10 + (9 + (8 + ...))
-- We can make it Tail Recursive by using an accumulator argument.
-- Tail recursive functions don't grow the call stack because the recursive call is the *very last* thing done.
-- Haskell (and GHC specifically) optimizes this into a fast imperative loop under the hood.

sumTailRecursive :: Int -> Int
sumTailRecursive n = go n 0
  where
    -- 'go' is a common naming convention for a recursive helper function
    go 0 acc = acc                         -- Base case: Return the accumulator
    go x acc = go (x - 1) (acc + x)        -- Tail call


-- 3. Infinite Lists and Lazy Evaluation
-- Haskell's killer feature: because values are only evaluated when needed,
-- we can declare infinite lists easily.

-- An infinite list of all positive integers:
infiniteNumbers :: [Int]
infiniteNumbers = [1..]

-- Taking the first 5 elements. `take` stops asking after 5 items.
firstFive :: [Int]
firstFive = take 5 infiniteNumbers

-- Summing them up.
sumFirstFive :: Int
sumFirstFive = sum firstFive


-- 4. Infinite recursive streams
-- Let's make an infinite Fibonacci sequence functionally.
-- This uses a beautifully elegant Haskell idiom combining infinite lists and zipWith.

fibs :: [Int]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
--  fibs:      0, 1, 1, 2, 3, 5,  8...
--  tail fibs: 1, 1, 2, 3, 5, 8, 13...
--  zipWith +: 1, 2, 3, 5, 8, 13, 21... (These become the rest of fibs)

first10Fibs :: [Int]
first10Fibs = take 10 fibs


main :: IO ()
main = do
    putStrLn $ "Recursive sum(10): " ++ show (sumRecursive 10)
    putStrLn $ "Tail-recursive sum(10): " ++ show (sumTailRecursive 10)
    putStrLn $ "Sum first five of infinite count: " ++ show sumFirstFive
    putStrLn $ "First 10 Fibonaccis: " ++ show first10Fibs
