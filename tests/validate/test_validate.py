from pytest import raises
from validate import password_entropy, hash_password, compare_password, parse_email, ValidationError


def test_password_entropy():
    """
    Test the entropy of a password.
    """
    entropy = password_entropy("this is a password")
    assert entropy > 0.66


def test_hash_password():
    """
    Test the hash_password method.
    """

    hashed_password = hash_password("this is a password")
    assert hashed_password is not None

    ok = compare_password("this is a password", hashed_password)
    assert ok is True


def test_hash_password_mismatch():
    """
    Test the hash_password method.
    """

    hashed = hash_password("this is a password")
    assert hashed is not None

    with raises(ValidationError):
        compare_password("this is not a password", hashed)


def test_validating_email():
    """
    Test the check_email method.
    """
    email = parse_email("test@mail.com")
    assert email == "test@mail.com"

    with raises(ValidationError):
        parse_email("test#mail.com")
