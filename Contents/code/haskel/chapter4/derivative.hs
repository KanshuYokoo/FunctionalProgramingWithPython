-- HOF that takes a function and returns its numerical derivative
derivative :: (Double -> Double) -> Double -> (Double -> Double)
derivative f dx = \x -> (f (x + dx) - f x) / dx

square :: Double -> Double
square x = x * x

cube :: Double -> Double
cube x = x * x * x

main :: IO ()
main = do
  -- f'(x) of x^2 at x = 3
  let fPrimeSquare = derivative square 1e-5
  print (fPrimeSquare 3.0) -- Approx 6.00001
  
  -- f'(x) of x^3 at x = 2
  let fPrimeCube = derivative cube 1e-5
  print (fPrimeCube 2.0) -- Approx 12.00001
