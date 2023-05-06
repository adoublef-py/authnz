from __future__ import annotations
from dataclasses import dataclass, field
from uuid import UUID, uuid4

from validate import hash_password, parse_email, ValidationError

@dataclass
class User:
    """
    User represents the user entity within the domain.
    """

@dataclass(frozen=True) # frozen=True makes the class immutable
class Credentials:
    """
    Credentials holds sensitive information about a user.
    """
    email: str
    password: bytes

    def parse_credentials(email: str, password: str) -> Credentials:
        """
        Parse untrusted data into a Credentials object.
        """
        try:
            hash = hash_password(password)  # hash the password
            email = parse_email(email)  # validate the email
        except ValidationError as e:
            raise e
        
        return Credentials(email, hash)
    
    def parse_dict(data: dict) -> Credentials:
        """
        Parse a dictionary into a Credentials object.
        """
        try:
            email = parse_email(data["email"])  # validate the email
            hash = data["password"]  # get the password
        except Exception as e:
            raise e
        return Credentials(email, hash)