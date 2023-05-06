from bcrypt import hashpw, gensalt, checkpw
from password_strength import PasswordPolicy
from email_validator import validate_email, EmailSyntaxError


def password_entropy(password: str, strength=0.66) -> float:
    """
    This function checks if a string is a valid password by attempting to
    check it's entropy.

    The default policy is to have a password with a strength of 0.66.
    """
    
    # A pretty good password will have a strength >= 0.66
    policy = PasswordPolicy.from_names(
        strength=strength)  

    password_stats = policy.password(password)

    if password_stats.strength() < strength:
        # TODO: include stats on why the password is weak
        raise ValidationError("Password is too weak")
    # just return the strength number
    return password_stats.strength()


def hash_password(password: str, strength=0.66) -> bytes:
    """
    Hash a password. An exception will be raised if the password
    is too weak.
    """
    try:
        password_entropy(password, strength)
    except Exception as e:
        raise e
    return hashpw(password.encode(), gensalt())


def compare_password(password: str, hashed_password: bytes) -> bool:
    """
    Compare a password with a hashed password. An exception will be
    raised if the passwords do not match.
    """
    if checkpw(password.encode(), hashed_password) is False:
        raise ValidationError("There is match with hashed password")
    return True


def parse_email(email: str) -> bool:
    """
    Check if an email is valid. If it is, return the normalized form.
    """
    try:
        address = validate_email(email)
        # normalized form
    except EmailSyntaxError:
        raise ValidationError("Is not a valid RFC 5322 email address")
    except Exception as e:
        raise e
    return address.normalized


class ValidationError(Exception):
    """
    This exception is raised when a validation fails
    """
    pass
