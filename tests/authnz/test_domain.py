from pytest import mark, raises
from contextlib import nullcontext as does_not_raise
from authnz import Credentials
from validate import ValidationError

@mark.parametrize("email, password, expected", [
    ("test@mail.com", "this is a valid password", does_not_raise()),
    ("test#mail.com", "this is a valid password", raises(ValidationError)),
    ("test#mail.com", "weak password", raises(ValidationError)),
])
def test_parsing_credentials(email: str, password: str, expected: Exception):
    with expected:
        creds = Credentials.parse_credentials(email=email, password=password)
        assert creds is not None
