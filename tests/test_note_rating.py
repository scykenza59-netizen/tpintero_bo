import pytest
from note_rating import rate_note
def test_rate_9_returns_unsuccessful():
    assert rate_note(9) == "unsuccessful"
@pytest.mark.parametrize("note", [8, 9])
def test_rate_note_unsuccessful(note):
    assert rate_note(note) == "unsuccessful"


def test_rate_10_returns_acceptable():
    assert rate_note(10) == "acceptable"


def test_rate_8_returns_unsuccessful():
    assert rate_note(8) == "unsuccessful"