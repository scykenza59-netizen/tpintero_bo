import pytest
from note_rating import rate_note

@pytest.mark.parametrize(
    "note, expected",
    [
        (7, "unsuccessful"),
        (8, "unsuccessful"),
        (9, "unsuccessful"),
        (10, "acceptable"),
        (11, "good"),
        (12, "good"),(13, "very good")
    ])
def test_note_result(note, expected):
    actual_result = rate_note(note)
    assert actual_result == expected

def test_rate_note_13_verygood():
    assert rate_note(13) == "very good"