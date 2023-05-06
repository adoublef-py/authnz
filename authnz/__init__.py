from __future__ import annotations
from dataclasses import dataclass, field
from uuid import UUID, uuid4

from validate import compare_password, hash_password, parse_email

@dataclass
class User:
    """
    User represents the user entity within the domain.
    """
    username: str = field(compare=False) # non-default arguments mustn't follow default arguments
    bio: str | None = field(default=None, compare=False) # is non-empty this must be validated
    photo_url: str | None = field(default=None, compare=False) # is non-empty this must be validated
    credentials: Credentials | None = field(default=None, compare=False) # unsure if I need to use the | operator here
    
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        if len(self.username) < 3 or len(self.username) > 20:
            raise ValueError("username must be between 3 and 20 characters")
        if self.bio is not None and len(self.bio) > 100:
            raise ValueError("bio must be less than 100 characters")

@dataclass(frozen=True) # frozen=True makes the class immutable
class Credentials:
    """
    Credentials holds sensitive information about a user.
    """
    email: str
    password: bytes

    def compare_password(self, password: str) -> bool:
        """
        Compare a password with a hashed password. An exception will be
        raised if the passwords do not match.
        """
        return compare_password(password, self.password)
    
def parse_credentials(email: str, password: str) -> Credentials:
    """
    Parse untrusted data into a Credentials object.
    """
    hash = hash_password(password)  # hash the password
    email = parse_email(email)  # validate the email

    return Credentials(email, hash)