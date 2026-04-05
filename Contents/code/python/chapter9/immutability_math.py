# The imperative view vs the mathematical pattern

# 1. Imperative (Time-bound, Mutative)
# In many languages we consider modifying variables normal:
my_list = [1, 2, 3]
my_list.append(4) # Mutates the list in-place over time

# 2. Functional / Mathematical (Timeless, Immutable)
# Instead of mutating an object, we map to a new object.
# Using a tuple guarantees it cannot be changed mathematically.
my_tuple = (1, 2, 3)

# We construct a new tuple using the old one, no mutation.
my_new_tuple = my_tuple + (4,) 

# Both my_tuple and my_new_tuple exist simultaneously and unchanging.
