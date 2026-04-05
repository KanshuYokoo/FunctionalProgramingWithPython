-- Structural Sharing in Haskell lists
module StructuralSharing where

-- Lists in Haskell are Singly Linked Lists
-- Prepending an element via the cons operator (:) is an O(1) operation
-- that reuses the tail of the existing list in memory!

baseList :: [Int]
baseList = [2, 3, 4]

-- The new element '1' just points to the head of 'baseList'.
-- There is no deep copy required! Both lists share memory.
newList :: [Int]
newList = 1 : baseList

-- In an imperative language, updating an "immutable" array 
-- might require an O(N) full deep-copy of the data. 
-- In Haskell, structural sharing guarantees both immutability and efficiency.
