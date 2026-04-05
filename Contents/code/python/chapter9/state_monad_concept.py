from typing import Tuple, List, TypeVar, Generic, Callable

# A simple conceptual demonstration of state transitions as pure functions
# mathematically modeled as S -> (A, S')
# where S is the state, A is the computation result.

S = TypeVar('S')
A = TypeVar('A')

class StateComputation(Generic[S, A]):
    def __init__(self, run_computation: Callable[[S], Tuple[A, S]]):
        self.run_computation = run_computation

    def bind(self, flat_mapper: Callable[[A], 'StateComputation[S, TypeVar("B")]']) -> 'StateComputation[S, TypeVar("B")]':
        """
        The Monadic 'bind' (>>=). It sequences two stateful computations 
        by threading the intermediate state cleanly behind the scenes.
        """
        def chained_computation(initial_state: S) -> Tuple[TypeVar("B"), S]:
            # Run the first computation to get an intermediate result and intermediate state
            result_a, intermediate_state = self.run_computation(initial_state)
            
            # Use the result to generate the next computation
            next_computation = flat_mapper(result_a)
            
            # Run the next computation with the intermediate state
            return next_computation.run_computation(intermediate_state)
            
        return StateComputation(chained_computation)

# Example: Maintaining a "counter" state without mutating variables
def pop_value() -> StateComputation[List[int], int]:
    """A computation that extracts a value from a stack state."""
    def compute(state: List[int]) -> Tuple[int, List[int]]:
        popped = state[0]
        new_state = state[1:] # We return a NEW state, we do not mutate inplace!
        return (popped, new_state)
    return StateComputation(compute)

def push_value(val: int) -> StateComputation[List[int], None]:
    """A computation that pushes a value onto a stack state."""
    def compute(state: List[int]) -> Tuple[None, List[int]]:
        new_state = [val] + state # Creating a new list
        return (None, new_state)
    return StateComputation(compute)

# Usage:
if __name__ == "__main__":
    # We compose the operations mathematically!
    # Let's push 3, push 5, then pop a value
    operations = push_value(3).bind(
        lambda _: push_value(5)
    ).bind(
        lambda _: pop_value()
    )

    initial_stack = []
    # Nothing has "changed" yet. We just have a formula.
    # Now we apply the initial state:
    result, final_stack = operations.run_computation(initial_stack)
    
    print(f"Result extracted: {result}")
    print(f"Final true State: {final_stack}")
    
    # We did not mutate lists in-place using .append() or .pop() !
