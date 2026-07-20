module Pascal where

-- 1. Tree Recursion
-- The direct translation of Pascal's Identity.
-- Recursion branches into two subcalls, building a call tree.
pascal :: Int -> Int -> Int
pascal 0 _ = 1
pascal c r
  | c == r    = 1
  | otherwise = pascal (c - 1) (r - 1) + pascal c (r - 1)


-- 2. Infinite Stream representation
-- Due to lazy evaluation, we can declare the entire infinite triangle
-- as a list of lists. Each row is computed from the previous row
-- using zipWith (+) over the shifted row.
pascalTriangle :: [[Int]]
pascalTriangle = iterate nextRow [1]
  where
    nextRow :: [Int] -> [Int]
    nextRow row = zipWith (+) (0 : row) (row ++ [0])


main :: IO ()
main = do
    putStrLn $ "pascal 2 4 = " ++ show (pascal 2 4)
    
    putStrLn "First 5 rows of infinite pascalTriangle:"
    -- Take the first 5 rows and print them
    mapM_ (print . show) (take 5 pascalTriangle)
