import pytest
from note_rating import rate_note
@pytest.mark.parametrize("note", [8, 9])
@pytest.mark.parametrize("note", [7, 8, 9])
def test_rate_note_unsuccessful(note):
    assert rate_note(note) == "unsuccessful"