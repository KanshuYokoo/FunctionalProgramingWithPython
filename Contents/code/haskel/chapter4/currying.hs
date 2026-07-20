-- Manual implementations of curry and uncurry (matching standard library)
curryManual :: ((a, b) -> c) -> a -> b -> c
curryManual f = \x y -> f (x, y)

uncurryManual :: (a -> b -> c) -> (a, b) -> c
uncurryManual f = \(x, y) -> f x y

-- Multi-argument function using tuples (uncurried)
addTuple :: (Int, Int) -> Int
addTuple (x, y) = x + y

-- Multi-argument function using currying
addCurried :: Int -> Int -> Int
addCurried x y = x + y

-- Practical logging function
logMessage :: String -> String -> IO ()
logMessage level message = putStrLn ("[" ++ level ++ "] " ++ message)

main :: IO ()
main = do
  -- Using curried addition
  let curriedAdd = curryManual addTuple
  let addFive = curriedAdd 5
  print (addFive 10) -- 15

  -- Using uncurried addition
  let uncurriedAdd = uncurryManual addCurried
  print (uncurriedAdd (5, 10)) -- 15

  -- Using curried logging configurations
  let infoLog = logMessage "INFO"
  let errorLog = logMessage "ERROR"
  infoLog "Haskell application started."
  errorLog "Haskell error encountered."
