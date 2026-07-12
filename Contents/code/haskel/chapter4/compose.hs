-- HOF that returns the composition of two functions manually
compose :: (b -> c) -> (a -> b) -> (a -> c)
compose f g = \x -> f (g x)

addOne :: Int -> Int
addOne x = x + 1

square :: Int -> Int
square x = x * x

main :: IO ()
main = do
  -- (square o addOne)(4) = (4 + 1)^2 = 25
  let squareOfAddOne = compose square addOne
  print (squareOfAddOne 4)
