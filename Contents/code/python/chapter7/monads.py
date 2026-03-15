from typing import TypeVar, Generic, Callable, Optional, Dict

T = TypeVar('T')
U = TypeVar('U')

class MaybeAsMonad(Generic[T]):
    """
    Extending our Maybe class to be a full Monad.
    It now has a 'bind' operation (often called flatMap in other languages).
    """
    def __init__(self, value: Optional[T]):
        self._value = value

    @property
    def is_present(self) -> bool:
        return self._value is not None

    def bind(self, func: Callable[[T], 'MaybeAsMonad[U]']) -> 'MaybeAsMonad[U]':
        """
        The bind ( >>= ) operation!
        Unlike map, which expects T -> U, bind expects T -> Maybe[U].
        Without bind, applying such a function with map would result
        in Maybe[Maybe[U]]. Bind "flattens" the context.
        """
        if self.is_present:
            return func(self._value)  # type: ignore
        return MaybeAsMonad(None)

    def __repr__(self) -> str:
        return f"Just({self._value})" if self.is_present else "Nothing()"


# --- A Practical Example: Database Lookups ---

# Our mock databases
users_db: Dict[int, str] = {
    1: "Alice",
    2: "Bob"
}

user_emails_db: Dict[str, str] = {
    "Alice": "alice@wonderland.com"
}

# Functions that might fail, returning a context (Monad)
def get_user_name(user_id: int) -> MaybeAsMonad[str]:
    name = users_db.get(user_id)
    return MaybeAsMonad(name)

def get_email(user_name: str) -> MaybeAsMonad[str]:
    email = user_emails_db.get(user_name)
    return MaybeAsMonad(email)

# --- The Monadic Chain ---

# Scenario 1: Everything succeeds
# Looking up user 1 ("Alice"), and then her email ("alice@wonderland.com")
email_for_user_1 = get_user_name(1).bind(get_email)
print(f"Email for User 1: {email_for_user_1}")

# Scenario 2: First step succeeds, second fails
# Looking up user 2 ("Bob"), who has no email in the DB.
# The chain safely skips executing get_email with a missing value.
email_for_user_2 = get_user_name(2).bind(get_email)
print(f"Email for User 2: {email_for_user_2}")

# Scenario 3: First step fails
# Looking up user 99 (Does not exist).
# The chain stops immediately. NoneType exceptions are impossible!
email_for_user_99 = get_user_name(99).bind(get_email)
print(f"Email for User 99: {email_for_user_99}")
