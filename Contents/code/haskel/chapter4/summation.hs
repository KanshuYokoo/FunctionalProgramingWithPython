-- Higher-order function for mathematical summation: sum_{n=a}^{b} f(n)
sumSeries :: (Int -> Int) -> Int -> Int -> Int
sumSeries f a b = sum [f n | n <- [a..b]]

-- Alternative recursive implementation
sumSeriesRec :: (Int -> Int) -> Int -> Int -> Int
sumSeriesRec f a b
  | a > b     = 0
  | otherwise = f a + sumSeriesRec f (a + 1) b

main :: IO ()
main = do
  -- Sum of identity function: 1 + 2 + 3 + 4 + 5 = 15
  let sumIdentity = sumSeries (\x -> x) 1 5
  
  -- Sum of squares: 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
  let sumSquares = sumSeries (\x -> x * x) 1 5
  
  -- Sum of cubes: 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225
  let sumCubes = sumSeriesRec (\x -> x * x * x) 1 5
  
  print sumIdentity
  print sumSquares
  print sumCubes
