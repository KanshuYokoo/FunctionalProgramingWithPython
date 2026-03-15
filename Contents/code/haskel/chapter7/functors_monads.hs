-- Haskell's native support for Category Theory concepts
-- We will explore Functors and Monads through the Maybe type.

-- The standard library defines Maybe roughly like this:
-- data Maybe a = Nothing | Just a

--------------------------------------------------------------------------------
-- 1. Functors (fmap)
--------------------------------------------------------------------------------
-- A Functor allows us to apply a normal function (a -> b) 
-- to a value wrapped in a context (f a) to get a new context (f b).

-- The type signature of fmap:
-- fmap :: Functor f => (a -> b) -> f a -> f b

square :: Int -> Int
square x = x * x

-- Example: Mapping square over a Just context
just25 :: Maybe Int
just25 = fmap square (Just 5)
-- Evaluates to: Just 25

-- Example: Mapping over a Nothing context safely
stillNothing :: Maybe Int
stillNothing = fmap square Nothing
-- Evaluates to: Nothing

--------------------------------------------------------------------------------
-- 2. Monads (bind / >>=)
--------------------------------------------------------------------------------
-- Monads allow us to chain computations that can fail (or return contexts).
-- What if our function returns a context itself? (a -> f b)
-- If we mapped it, we'd get (f (f b)). We need a way to flatten it.

-- The type signature of bind (>>=):
-- (>>=) :: Monad m => m a -> (a -> m b) -> m b

-- Mock databases using pure functions returning contexts
getUserName :: Int -> Maybe String
getUserName 1 = Just "Alice"
getUserName 2 = Just "Bob"
getUserName _ = Nothing

getEmail :: String -> Maybe String
getEmail "Alice" = Just "alice@wonderland.com"
getEmail _       = Nothing

-- Example: The Monadic Chain
-- Looking up user 1, then extracting their name and passing it to getEmail
emailForUser1 :: Maybe String
emailForUser1 = getUserName 1 >>= getEmail
-- Evaluates to: Just "alice@wonderland.com"

-- If any step fails, the whole chain returns Nothing without throwing an error
emailForUser2 :: Maybe String
emailForUser2 = getUserName 2 >>= getEmail
-- Evaluates to: Nothing (Bob has no email)

emailForUser99 :: Maybe String
emailForUser99 = getUserName 99 >>= getEmail
-- Evaluates to: Nothing (User 99 does not exist)

--------------------------------------------------------------------------------
-- 3. The "do" syntax
--------------------------------------------------------------------------------
-- Haskell provides "do" notation as syntactical sugar for monadic chains,
-- making contextual sequences look like imperative procedural code!

getEmailImperatively :: Int -> Maybe String
getEmailImperatively userId = do
    name  <- getUserName userId  -- Extract String from Maybe String (if Just)
    email <- getEmail name       -- Pass it forward
    return email                 -- Wrap it back up (though getEmail already returns Maybe)
    
-- Identical logic, different syntax:
-- getEmailImperatively 1  => Just "alice@wonderland.com"
-- getEmailImperatively 99 => Nothing
