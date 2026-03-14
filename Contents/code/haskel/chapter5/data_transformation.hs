module DataTransformation where

-- 1. Mapping (Data Transformation)
-- Applying a function to every item in a list.

numbers :: [Int]
numbers = [1, 2, 3, 4, 5]

square :: Int -> Int
square x = x * x

-- Using built-in map
-- Type signature of map: (a -> b) -> [a] -> [b]
squaredNumbersMap :: [Int]
squaredNumbersMap = map square numbers
-- Expected: [1, 4, 9, 16, 25]

-- Pythonic alternative equivalent: List Comprehension
squaredNumbersComp :: [Int]
squaredNumbersComp = [square x | x <- numbers]


-- 2. Filtering
-- Keeping items that satisfy a predicate.

isEven :: Int -> Bool
isEven x = x `mod` 2 == 0

-- Using built-in filter
-- Type signature of filter: (a -> Bool) -> [a] -> [a]
evenNumbersFilter :: [Int]
evenNumbersFilter = filter isEven numbers
-- Expected: [2, 4]

-- List Comprehension with condition
evenNumbersComp :: [Int]
evenNumbersComp = [x | x <- numbers, isEven x]


-- 3. Reducing (Folding)
-- Accumulating items down to a single value.

add :: Int -> Int -> Int
add x y = x + y

-- Using foldl (left fold)
-- Type signature of foldl: (b -> a -> b) -> b -> [a] -> b
-- It takes an accumulator function, an initial value, and a list.
sumFoldl :: Int
sumFoldl = foldl add 0 numbers
-- Expected: 15

-- Using foldr (right fold)
-- Type signature of foldr: (a -> b -> b) -> b -> [a] -> b
sumFoldr :: Int
sumFoldr = foldr add 0 numbers
-- Expected: 15


-- 4. Defining our own Map and Filter with recursion

myMap :: (a -> b) -> [a] -> [b]
myMap _ [] = []
myMap f (x:xs) = f x : myMap f xs

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter _ [] = []
myFilter p (x:xs)
    | p x       = x : myFilter p xs
    | otherwise = myFilter p xs


-- 5. Combining Map and Filter
-- Square only the even numbers

-- Functional composition style (.)
-- Note: Function composition is read right-to-left
squaredEvensFunc :: [Int]
squaredEvensFunc = map square (filter isEven numbers)

-- Using the composition operator
squaredEvensCompose :: [Int]
squaredEvensCompose = (map square . filter isEven) numbers

-- List Comprehension style
squaredEvensComp :: [Int]
squaredEvensComp = [square x | x <- numbers, isEven x]

main :: IO ()
main = do
    putStrLn $ "Original: " ++ show numbers
    putStrLn $ "Map (square): " ++ show squaredNumbersMap
    putStrLn $ "Filter (even): " ++ show evenNumbersFilter
    putStrLn $ "Fold (sum): " ++ show sumFoldl
    putStrLn $ "Combined (square evens): " ++ show squaredEvensFunc
