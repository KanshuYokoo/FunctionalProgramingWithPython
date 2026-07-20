-- Purely Functional Sets as Characteristic Functions
-- Inspired by Martin Odersky's course: Functional Programming Principles in Scala (EPFL)
module FuncSet where

type FunSet = Int -> Bool

contains :: FunSet -> Int -> Bool
contains s elem = s elem

singletonSet :: Int -> FunSet
singletonSet elem = \x -> x == elem

union :: FunSet -> FunSet -> FunSet
union s t = \x -> s x || t x

intersect :: FunSet -> FunSet -> FunSet
intersect s t = \x -> s x && t x

diff :: FunSet -> FunSet -> FunSet
diff s t = \x -> s x && not (t x)

filterSet :: FunSet -> (Int -> Bool) -> FunSet
filterSet s p = \x -> s x && p x

forall :: FunSet -> (Int -> Bool) -> Int -> Bool
forall s p bound = iter (-bound)
  where
    iter a
      | a > bound                 = True
      | contains s a && not (p a) = False
      | otherwise                 = iter (a + 1)

exists :: FunSet -> (Int -> Bool) -> Int -> Bool
exists s p bound = not $ forall s (\x -> not (p x)) bound

mapSet :: FunSet -> (Int -> Int) -> Int -> FunSet
mapSet s f bound = \y -> exists s (\x -> f x == y) bound
