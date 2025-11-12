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
        (12, "good"),(13, "very good"),(14, "veryVery good"),
(15,"veryVery good")
    ])
def test_note_result(note, expected):
    actual_result = rate_note(note)
    assert actual_result == expected

