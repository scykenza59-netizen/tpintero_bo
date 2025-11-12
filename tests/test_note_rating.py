import pytest
from note_rating import rate_note

@pytest.mark.parametrize(
    "note, expected",
    [
        (7, "unsuccessful"),
        (8, "unsuccessful"),
        (9, "unsuccessful"),
        (10, "acceptable"),
        (11, "acceptable"),
        (12, "good"),
    ])
def test_note_result(note, expected):
    actual_result = rate_note(note)
    assert actual_result == expected

