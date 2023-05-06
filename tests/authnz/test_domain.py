from pytest import mark, raises, fixture
from contextlib import contextmanager, nullcontext as does_not_raise
from uuid import UUID
from authnz import User, Credentials, parse_credentials
from validate import ValidationError

@mark.parametrize("email, password, expected", [
    ("test@mail.com", "this is a valid password", does_not_raise()),
    ("test#mail.com", "this is a valid password", raises(ValidationError)),
    ("test#mail.com", "weak password", raises(ValidationError)),
])
def test_parsing_credentials(email: str, password: str, expected: contextmanager):
    with expected:
        creds = parse_credentials(email=email, password=password)
        assert creds is not None


@fixture
def valid_credentials():
    email, password = ("test@mail.com", "this is a valid password")
    return parse_credentials(email, password)

@mark.parametrize("password, expected", [
    ("this is a valid password", does_not_raise()),
    ("this is a wrong password", raises(ValidationError)),
])
def test_password_match(valid_credentials: Credentials, password: str, expected: contextmanager):
    with expected: 
        matched = valid_credentials.compare_password(password)
        assert matched is True

@mark.parametrize("username, bio, expected", [
    ("test", None, does_not_raise()),
    ("test", "Simple Bio", does_not_raise()),
    ("test", "Simple Bio".ljust(101, "O"), raises(ValueError)),
    ("t", None, raises(ValueError)),
])
def test_user_entity(valid_credentials: Credentials, username: str, bio: str | None, expected: contextmanager):
    with expected:
        user = User(username=username, bio=bio, credentials=valid_credentials)
        assert user is not None
        assert UUID(str(user.id)) is not None