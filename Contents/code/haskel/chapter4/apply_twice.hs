-- A simple pure function
addOne :: Int -> Int
addOne x = x + 1

multiplyByTwo :: Int -> Int
multiplyByTwo x = x * 2

-- HIGHER-ORDER FUNCTION
-- Takes a function (Int -> Int) and an Int, returns an Int
applyTwice :: (Int -> Int) -> Int -> Int
applyTwice f x = f (f x)

main :: IO ()
main = do
  print (applyTwice addOne 5)         -- 7
  print (applyTwice multiplyByTwo 5) -- 20
