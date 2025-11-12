import pytest
from note_rating import rate_note

@pytest.mark.parametrize("note", [7, 8, 9])
def test_rate_note_unsuccessful(note):
    assert rate_note(note) == "unsuccessful"
def test_rate_12_is_good():
    assert rate_note(12) == "good"
