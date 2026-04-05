-- Example Morphisms
myLength :: String -> Int
myLength s = length s

isEven :: Int -> Bool
isEven n = n `mod` 2 == 0

-- Using the built-in composition operator (.) 
-- (isEven composed with myLength) : String -> Bool
isEvenLength :: String -> Bool
isEvenLength = isEven . myLength

main :: IO ()
main = print (isEvenLength "Category") -- True
